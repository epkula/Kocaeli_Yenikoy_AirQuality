# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 14:47:51 2025

@author: elifb
"""

# Kocaeli Yeniköy Air Quality Analysis - Kaggle Notebook
import pandas as pd
import matplotlib.pyplot as plt

# Kaggle dataset path (after uploading dataset)
data = pd.read_excel("C:/Users/elifb/Downloads/deneme.1.xlsx", header=0)

# Preview first 5 rows
print("Data Preview:")
print(data.head())

# Convert 'Tarih' column to datetime
data['Tarih'] = pd.to_datetime(data['Tarih'], dayfirst=True, errors='coerce')

# Select numeric columns
numeric_cols = data.columns.drop('Tarih')

# Replace comma with dot and convert to numeric
for col in numeric_cols:
    data[col] = pd.to_numeric(data[col].astype(str).str.replace(',', '.'), errors='coerce')

print("\nColumn Data Types:")
print(data.dtypes)
print("\nCleaned Data Preview:")
print(data.head())

# Calculate average values
print("\nAverage Values:")
for col in numeric_cols:
    avg = data[col].mean()
    print(f"{col} average: {avg:.2f} µg/m3")

# Calculate maximum values and their timestamps
max_list = []

print("\nMaximum Values:")
for col in numeric_cols:
    max_idx = data[col].idxmax()
    max_value = data.loc[max_idx, col]
    max_time = data.loc[max_idx, 'Tarih']
    print(f"{col} maximum: {max_value:.2f} µg/m3, time: {max_time}")
    max_list.append({
        "Pollutant": col,
        "Maximum Value (µg/m3)": max_value,
        "Time": max_time
    })

# Create a table of maximum values
max_table = pd.DataFrame(max_list)
print("\nMaximum Values Table:")
print(max_table)

# Set 'Tarih' as the index
data.set_index('Tarih', inplace=True)

# Line plot of pollutants over time
plt.figure(figsize=(12,6))
for col in numeric_cols:
    plt.plot(data.index, data[col], label=col)

plt.xlabel('Time')
plt.ylabel('Value (µg/m3)')
plt.title('Hourly Pollutant Concentration Changes')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
