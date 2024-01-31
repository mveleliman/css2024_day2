# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 08:28:07 2024

@author: Mveleli Manitshana
"""
#Import Country Data Index using Relative Path
import pandas as pd
df = pd.read_csv("country_data_index.csv")

#Importing from online
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)

#importing various data files.
df = pd.read_csv("Geospatial Data.txt",sep=";")


file = pd.read_excel("Residentdoctors.xlsx")
file = pd.read_json("student_data.json")
print(file)
