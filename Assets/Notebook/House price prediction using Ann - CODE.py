# -*- coding: utf-8 -*-
"""California_housing_price_project(2333265040).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qIuaWVLT4u-TmPysq4nWu5N_Cd_a1efx

#Import Libraries
"""

# importing libraries needed for data manipulation and preprocessing
# other libraries and component will be imported as they needed like ( sklearn modules) and others like (keras) wich is build in tensorflow framework
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf

"""#Data Acquisition and Preprocessing

##1. Obtain the Data
"""

Housing_df = pd.read_csv("housing.csv")

"""## 2. Explore the Data"""

# Looking at the first three records of the data
# and we can simply say that all features are different in scaling
Housing_df.head(3)

# By looking at this info() function we can see that there is a missing value of the "total_bedrooms" columns
# and  the data contain categorical column "ocean_proximity" which is not suitable for this regression problem
# We will decide later if we are going to drop it or "One-hot-encoding" it
Housing_df.info()

print('..................counting numbers of missing values.....................'),
Housing_df.isna().sum()  # Counting the number of missing values to see if it is ok to drop them

# Looking at this describe() method we can see that there is a large difference in the mean and the max value of some features
# We will look later for the outliers that can affect our model performance
Housing_df.describe()

#visualizing the null or undefinde values
sns.heatmap(Housing_df.drop("ocean_proximity",axis = 1).isnull(),yticklabels= False, cbar = False , cmap= "viridis" )

sns.heatmap(Housing_df.drop("ocean_proximity",axis=1).corr(),cmap = "viridis")

sns.pairplot(Housing_df) # Looking at the bottom right corner we can see that the median house value column contains outliers that make i non normally distributed

"""##3. Preprocess the Data

###dealing with missing values
"""

Housing_df['total_bedrooms'].fillna(Housing_df['total_bedrooms'].mean(),inplace= True) # Filling the missing values with the mean of their column

"""###cleaning the outliers"""

# Using the inter quartile range method (IQR) to clean the outliers

Q1 = Housing_df.drop(['ocean_proximity','longitude'], axis = 1).quantile(0.25)  #droping the logitude column because of the negative values
Q3 = Housing_df.drop(['longitude','ocean_proximity'], axis = 1).quantile(0.90)  #choosing 90% of the data as the third quartile to reduce overfitting

IQR = Q3 - Q1

up_bound = Q3 + 1.5 * IQR
low_bound = Q1 - 1.5 * IQR

# looping over every feature do check for the condition which is that the value does not go over the upper_bound nor below the low_bound

for feature in Housing_df.columns:
    if feature not in['longitude','ocean_proximity']:
        condition = (Housing_df[feature] < up_bound[feature]) & (Housing_df[feature] > low_bound[feature])
        Housing_df[feature] = Housing_df[condition][feature]

# Looping again to fill all the missing values caused by the previous function

for feature in Housing_df.columns:
    if feature not in ['longitude','ocean_proximity']:
        Housing_df[feature].fillna(Housing_df[feature].mean(),inplace=True)
Housing_df.info()

Housing_df.describe()

"""###Spliting the dataset into test and training sets"""

from sklearn.model_selection import train_test_split

X = Housing_df.drop(['ocean_proximity','median_house_value'],axis = 1)

#Drop the categorical feature

#( note : we could one-hot encoded it but that will be a problem later after scaling )

y = Housing_df['median_house_value']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) # splitting the data into training set and test set wich is 30% of the original data set

"""###Scaling the features using MinMax scaler"""

# Using the min max scaler to normalize the data

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

scaler.fit(X_train)  # We trained the scaler only on the training data to prevent any data leakage which is a good practice

X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

"""#Building the ANN Model

* We will perform different **experiments** to see the optimal choices for hyperparameters and architecture

## 1. Model_1

* **model_1** is the first model we will start simple and increase the complexity in the other models to see if their is going to be any improvment

###1. Define Model_1 Architecture
"""

model_1 = tf.keras.Sequential([
    tf.keras.layers.Dense(10),
    tf.keras.layers.Dense(1),
])

model_1.compile(
                loss = tf.keras.losses.mae,
                optimizer = tf.keras.optimizers.Adam(lr= 0.001) # Starting with a small learning reate
                )

# note we preferred to use the "Adam" optimizer over the "stochastic gradient descent" due to its performance over different types of ANN's

"""### 2. Model_1 training"""

history = model_1.fit(X_train,y_train,epochs = 300) # due to its simplicity and the small learning rate we increased the number of epochs

"""### 3. Model_1 evaluation"""

predictions1 = model_1.predict(X_test_scaled)  # predicting from the model

tf.keras.losses.mae(y_test,predictions1.reshape(y_test.shape)) # evaluating the model

"""##2. Model_2

* In this model we increased the complexity of the model to see if it was going to do better or worse and the changing the parameters in the next experiments

###1. Define Model_2 Architecture
"""

model_2 = tf.keras.Sequential([
    tf.keras.layers.Dense(60,activation='relu',input_shape=(8,)),
    tf.keras.layers.Dense(60,activation='relu'),
    tf.keras.layers.Dense(1,activation='relu')
])

model_2.compile(
    loss=tf.keras.losses.mae,
    optimizer=tf.keras.optimizers.Adam(learning_rate = 0.01),
    metrics = ["mae"]
)

"""###2. Model_2 training"""

history2 = model_2.fit(X_train_scaled,y_train,batch_size=25,epochs=100)  # we added a new parameter which is the "batch_size" to controle the amount of the data that the model see in one iteration

"""###3. Model_2 evaluation"""

predictions2 = model_2.predict(X_test_scaled)
tf.keras.losses.mae(y_test,predictions2.reshape(y_test.shape))

"""##3. Model 3

###1. Define Model_3 Architecture
"""

model_3 = tf.keras.Sequential([
    tf.keras.layers.Dense(60,activation='relu',input_shape=(8,)),
    tf.keras.layers.Dense(60,activation='relu'),
    tf.keras.layers.Dense(60,activation='relu'),
    tf.keras.layers.Dense(60,activation='relu'),
    tf.keras.layers.Dense(1,activation='linear')
])

model_3.compile(
    loss=tf.keras.losses.mae,
    optimizer=tf.keras.optimizers.Adam(learning_rate = 0.01),
    metrics = ["mae"]
)

"""###2. Model_3 training"""

history3 = model_3.fit(X_train_scaled,y_train,batch_size=32,epochs=100)

"""###3. Model_3 evaluation"""

predictions3 = model_3.predict(X_test_scaled)

tf.keras.losses.mae(y_test,predictions3.reshape(y_test.shape))

"""##Model_4

###1. Define Model_4 Architecture
"""

from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau

model_4 = tf.keras.Sequential([
    tf.keras.layers.Dense(60,activation='relu',input_shape=(8,)),
    tf.keras.layers.Dense(60,activation='relu'),
    tf.keras.layers.Dense(60,activation='relu'),
    tf.keras.layers.Dense(60,activation='relu'),
    tf.keras.layers.Dense(1,activation='linear')
])

model_4.compile(
    loss=tf.keras.losses.mae,
    optimizer=tf.keras.optimizers.Adam(learning_rate = 0.01),
    metrics = ["mae"]
)

# We will add two callbacks and try to optimise the performance of the model

early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
lr_scheduler = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=5)

"""###2. Model_4 training"""

history4 = model_4.fit(X_train_scaled,y_train,batch_size=32,epochs=100,callbacks=[early_stopping, lr_scheduler]) # Adding the two callbacks

"""###3. Model_4 evaluation"""

predictions4 = model_4.predict(X_test_scaled)
tf.keras.losses.mae(y_test,predictions4.reshape(y_test.shape))

"""#comparing the models performance"""

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np


models = [model_1, model_2, model_3, model_4]
model_names = ['Model 1', 'Model 2', 'Model 3', 'Model 4']
results = {}

for i, model in enumerate(models):
    y_pred_test = model.predict(X_test_scaled)

    print(model_names[i])
    print('test_mae  :',mean_absolute_error(y_test, y_pred_test.reshape(y_test.shape))),
    print('test_mse  :' ,mean_squared_error(y_test, y_pred_test.reshape(y_test.shape))),
    print('test_r2   :' ,r2_score(y_test, y_pred_test.reshape(y_test.shape)))

import matplotlib.pyplot as plt

history_list = [history, history2, history3, history4]

# Plot loss curves

plt.figure(figsize=(12, 8))

for i, history in enumerate(history_list):
    plt.plot(history.history['loss'], label=f'{model_names[i]} Training Loss')
plt.title('Loss Curves')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

plt.figure(figsize=(12, 8))
for i, model in enumerate(models):
    y_pred = model.predict(X_test)
    plt.scatter(y_test, y_pred, alpha=0.5, label=f'{model_names[i]}')
plt.title('Predicted vs Actual Values')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.legend()
plt.show()

import seaborn as sns

plt.figure(figsize=(12, 8))

sns.histplot(y_test - predictions1.reshape(y_test.shape), alpha=0.5, kde=True, label='model1')
sns.histplot(y_test - predictions2.reshape(y_test.shape), alpha=0.5, kde=True, label='model2')
sns.histplot(y_test - predictions3.reshape(y_test.shape), alpha=0.5, kde=True, label='model3')
sns.histplot(y_test - predictions4.reshape(y_test.shape), alpha=0.5, kde=True, label='{model4')

plt.title('Prediction Error Distribution')
plt.xlabel('Prediction Error')
plt.legend()

sns.displot(y_test - predictions1.reshape(y_test.shape))

sns.displot(y_test - predictions2.reshape(y_test.shape))

sns.displot(y_test - predictions3.reshape(y_test.shape))

sns.displot(y_test - predictions4.reshape(y_test.shape))
# We can see that model_4 residuals are centered around zero more than the other models

