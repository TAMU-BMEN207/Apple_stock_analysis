#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 21:20:18 2021

@author: annicenajafi

Description: In this example we take a look at Apple's stock prices and write a
program to plot an OHLC chart. To learn more about OHLC plots visit 
https://www.investopedia.com/terms/o/ohlcchart.asp

#Dataset Source:
    downloaded from Kaggle ==> https://www.kaggle.com/meetnagadia/apple-stock-price-from-19802021?select=AAPL.csv
    
#Make sure you have studied: Numpy, Matplotlib, Pandas

"""

#import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Read csv file using pandas
df = pd.read_csv("/Users/annicenajafi/Downloads/AAPL.csv")

#let's take a look at our data
df.head()

'''
Let's only look at recent data more specifically from 2020 to the most recent data
But first we have to convert our date column to datetime type so we would be able to 
treat it as date
'''
df['Date'] = pd.to_datetime(df['Date'])

df = df[df['Date'].dt.year > 2020] 
#Hold on let's look at the dataframe again
df.head()
#Hmmm... Do you see that the index starts at 10100?
#Question: what problems may it cause if we don't reset the index?!
#Let's fix it so it starts from 0 like the original df
df.reset_index(inplace=True)
df.head()


#Let's define the x axis
x_vals = np.arange(0,len(df['Date']))
fig, ax = plt.subplots(1, figsize=(50,10))

'''
Let's iterate through the rows and plot a candle stick for every date
What we do is we plot a vertical line that starts from the low point and ends
at the high point for every date
'''
for idx, val in df.iterrows():
    #Change the color to red if opening price is more than closing price 
    #Otherwise change it to green
    if val['Open'] > val['Close']: 
        col = 'red'
    else:
        col ='green'
    
    plt.plot([x_vals[idx], x_vals[idx]], [val['Low'], val['High']], color=col)
    #add a horizontal line to the left to show the openning price
    plt.plot([x_vals[idx], x_vals[idx]-0.05], 
             [val['Open'], val['Open']], 
             color=col)
    #add a horizontal line to the right to show the closing price
    plt.plot([x_vals[idx], x_vals[idx]+0.05], 
             [val['Close'], val['Close']], 
             color=col)

#Change the x axis tick marks
plt.xticks(x_vals[::50], df.Date.dt.date[::50])  
#change the y label 
plt.ylabel('USD')
#Change the title of the plot
plt.title('Apple Stock Price', loc='left', fontsize=20)
#let's show the plot

plt.show()



'''
Texas A&M University
BMEN 207
Fall 2021
'''


