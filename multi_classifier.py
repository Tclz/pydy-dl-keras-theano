#!/usr/bin/env python
# -*- coding: utf-8 -*-

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import applications,optimizers,Model
from keras.callbacks import ModelCheckpoint
# from keras.models import model_from_json

# dimensions of our images.
img_width, img_height = 150, 150
train_data_dir = 'data/train'
validation_data_dir = 'data/validation'
nb_train_samples = 38167
nb_validation_samples = 9426
epochs = 50
batch_size = 32

model_vgg = applications.VGG16(weights='imagenet', include_top=False, input_shape=(3, 150, 150))
top_model = Sequential()
top_model.add(Flatten(input_shape=model_vgg.output_shape[1:]))
top_model.add(Dense(256, activation='relu'))
top_model.add(Dropout(0.5))
top_model.add(Dense(20, activation='softmax'))

model = Model(inputs=model_vgg.input, outputs=top_model(model_vgg.output))
model.summary()

model.load_weights("model/multiClassifier-weights-improvement-01-0.349.h5")
for layer in model_vgg.layers[:15]:
    layer.trainable = False

model.compile(loss='categorical_crossentropy',
              optimizer=optimizers.SGD(lr=1e-4, momentum=0.9),
              metrics=['accuracy'])

print("Created model and loaded weights from file")

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical'
    )

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical'
    )

# bottleneck_features_train = model_vgg.predict_generator(train_generator, nb_train_samples // batch_size)
# np.save(open('models/bottleneck_features_train.npy', 'wb'), bottleneck_features_train)
#
# bottleneck_features_validation = model_vgg.predict_generator(validation_generator, nb_validation_samples // batch_size)
# np.save(open('models/bottleneck_features_validation.npy', 'wb'), bottleneck_features_validation)
#

filepath="model/multiClassifier-weights-improvement-{epoch:02d}-{val_acc:.3f}.h5"
# 每次epoch之后，如果验证误差减少，则保存模型数据
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=2, save_best_only=True,mode='max')
callbacks_list = [checkpoint]

model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples // batch_size,
    callbacks=callbacks_list
)

model.evaluate_generator(validation_generator, nb_validation_samples)
# 同时保存model和权重
# model.save('first_model.h5')
# 保存model
# model_json = model.to_json()
# with open("model.json", "w") as json_file:
#     json_file.write(model_json)

# 载入model ,读取json文件
# json_string = open('model.json').read()
# model = model_from_json(json_string)

