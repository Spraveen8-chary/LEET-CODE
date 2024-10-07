# num = 2222333344
# def count_reperted_number(num):
#     num = str(num)
#     result = ''
#     count = 1
#     for i in range(1, len(num)):
#         if num[i] == num[i-1]:
#             count += 1
#         else:
#             result += str(count) + num[i-1]
#             count = 1
    
#     result += str(count) + num[-1]
#     return result
# print(count_reperted_number(num))


import numpy as np
import pandas as pd
import os
from PIL import Image
import pickle
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

train_csv = pd.read_csv('/kaggle/input/morph/Dataset/Index/Train.csv')
test_csv = pd.read_csv('/kaggle/input/morph/Dataset/Index/Test.csv')
validation_csv = pd.read_csv('/kaggle/input/morph/Dataset/Index/Validation.csv')

IMAGES_PATH = '/kaggle/input/morph/Dataset/Images/Train/'

train_csv.head(3)

test_csv.head(3)

validation_csv.head(3)

train_subset = train_csv.sample(n = 4000, random_state = 42)
train_subset.head(3)

def processing_image(filepath, target_size = (224, 224)):
    img = Image.open(filepath)
    img_resized = img.resize(target_size)
    img_array = np.array(img_resized) / 255.0
    return img_array

def display_image(filepath):
    image = processing_image(filepath)
    plt.imshow(image)
    plt.axis('off')
    plt.show()

sample = train_subset.filepath.iloc[0]
print(sample)
display_image(sample)

train_subset.shape

train_images = []
train_ages = train_subset.age.tolist()

for file in train_subset['filepath']:
    img = processing_image(file)
    train_images.append(img)

train_images = np.array(train_images)
train_ages = np.array(train_ages)

from sklearn.model_selection import train_test_split

X_train, X_val, y_train, y_val = train_test_split(train_images, train_ages, test_size=0.2, random_state=42)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D(pool_size=(2, 2)),
    
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='linear')
])

model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_val, y_val))

val_loss, val_mae = model.evaluate(X_val, y_val)
print(f'Validation Loss: {val_loss}, Validation MAE: {val_mae}')

predicted_age = model.predict(X_val[:5])
predicted_age = np.clip(predicted_age, 0, None) 
print(predicted_age)

train_subset.filename.iloc[:5]

samples = IMAGES_PATH + train_subset.filename.iloc[:5]

for i in samples:
    display_image(i)

