#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 12:59:46 2019

@author: birnesh
"""
#import statements

import numpy as np 
import pandas as pd 

import random as rn

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns

#getting the data
X_test = pd.read_csv("/home/birnesh/Documents/MNIST/inputs/test.csv")
train = pd.read_csv("/home/birnesh/Documents/MNIST/inputs/train.csv")

#splitig the train data
y_train = train["label"]
X_train = train.drop(["label"], axis=1)
print(X_train.iloc[:,10:20].describe())
#Normalization
X_train = X_train/255
X_test = X_test/255
print(X_train.iloc[:,10:20].describe())
#print("X:")
#print(X_train.info())
#print("*"*50)
#print("X_test:")
#print(X_test.info())
#print("*"*50)
#print("y_train:")
#print(y_train.shape)