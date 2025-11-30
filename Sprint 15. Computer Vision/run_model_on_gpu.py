
import pandas as pd

import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Flatten
from tensorflow.keras.optimizers import Adam


def load_train(path):
    """Load the training part of the dataset from `path`.

    Uses labels.csv and images from the final_files/ folder.
    """
    labels = pd.read_csv(path + 'labels.csv')

    datagen = ImageDataGenerator(
        rescale=1.0/255,
        validation_split=0.25
    )

    train_datagen_flow = datagen.flow_from_dataframe(
        dataframe=labels,
        directory=path + 'final_files/',
        x_col='file_name',
        y_col='real_age',
        target_size=(224, 224),
        batch_size=32,
        class_mode='raw',
        subset='training',
        seed=12345
    )

    return train_datagen_flow


def load_test(path):
    """Load the validation/test part of the dataset from `path`."""
    labels = pd.read_csv(path + 'labels.csv')

    datagen = ImageDataGenerator(
        rescale=1.0/255,
        validation_split=0.25
    )

    test_datagen_flow = datagen.flow_from_dataframe(
        dataframe=labels,
        directory=path + 'final_files/',
        x_col='file_name',
        y_col='real_age',
        target_size=(224, 224),
        batch_size=32,
        class_mode='raw',
        subset='validation',
        seed=12345
    )

    return test_datagen_flow


def create_model(input_shape):
    """Define and compile the CNN model for age prediction."""
    backbone = ResNet50(
        input_shape=input_shape,
        weights='imagenet',
        include_top=False
    )
    backbone.trainable = False

    model = Sequential([
        backbone,
        GlobalAveragePooling2D(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(1)
    ])

    optimizer = Adam(learning_rate=3e-4)
    model.compile(
        optimizer=optimizer,
        loss='mae',
        metrics=['mae']
    )

    return model


def train_model(model, train_data, test_data,
                batch_size=None, epochs=20,
                steps_per_epoch=None, validation_steps=None):
    """Train the model using the provided generators."""

    if steps_per_epoch is None:
        steps_per_epoch = len(train_data)
    if validation_steps is None:
        validation_steps = len(test_data)

    model.fit(
        train_data,
        validation_data=test_data,
        epochs=epochs,
        steps_per_epoch=steps_per_epoch,
        validation_steps=validation_steps,
        verbose=2
    )

    return model


