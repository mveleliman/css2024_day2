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


#Date
df = pd.read_csv("time_series_data.csv",index_col=0)
print(df.info())

df['Date'] = pd.to_datetime(df['Date'])
print(df.info())

df['Year'] = df['Date'].dt.year
df = pd.read_csv("patient_data_dates.csv")
df = pd.read_csv("patient_data_dates.csv", index_col=0)
df['Date'] = df['Date'].replace({' ': '-'})
df.drop(index=26, inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
print(df.info())
avg_cal = df["Calories"].mean()
df["Calories"].fillna(avg_cal, inplace=True)

# Best Practice
df.dropna(inplace = True)
df = df.reset_index(drop=True)
#df.loc[7, 'Duration'] = 45
df.loc[7, 'Duration'].replace([450],50)
print(df)
#pd.set_option('display.max_rows',None)
##################
file = pd.read_csv("iris.csv")
print(file.columns)
col_names = file.columns.tolist
file["sepal_length_sq"] = file["sepal_length_sq"]**2
file["sepal_length_sq"] = file["sepal_length_sq"].apply(lambda x: x**2)
grouped = file.groupby("class")
mean_square_values = grouped['sepal_length_sq'].mean()
print(mean_square_values)
########

df1  = pd.read_csv('person_education.csv')
df2  = pd.read_csv('person_work.csv')

#inner join

# df_merger_inner = pd.merge(df1,df2,on="id")
print(file)
 df["class"] = df["class"].str.replace("Iris-", "")
 





