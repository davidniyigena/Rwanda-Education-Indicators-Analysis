# Rwanda Education Indicators Analysis
# Data Cleaning and Exploratory Data Analysis
# Author: David Niyigena

import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("../data/rwanda_education_indicators.csv")

# Preview data
print("First five rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nDataset information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Check duplicate records
duplicate_count = df.duplicated().sum()
print(f"\nDuplicate records: {duplicate_count}")

# Summary statistics
print("\nSummary statistics:")
print(df["value"].describe())

# Average value by indicator
indicator_summary = (
    df.groupby("indicator_name")["value"]
    .mean()
    .reset_index()
    .sort_values(by="value", ascending=False)
)

print("\nAverage value by indicator:")
print(indicator_summary)

# Average value by category
category_summary = (
    df.groupby("category")["value"]
    .mean()
    .reset_index()
    .sort_values(by="value", ascending=False)
)

print("\nAverage value by category:")
print(category_summary)

# Trend by year and category
year_category_trend = (
    df.groupby(["year", "category"])["value"]
    .mean()
    .reset_index()
)

print("\nTrend by year and category:")
print(year_category_trend.head())

# Education level summary
education_level_summary = (
    df.groupby("education_level")["value"]
    .mean()
    .reset_index()
    .sort_values(by="value", ascending=False)
)

print("\nAverage value by education level:")
print(education_level_summary)

# Save cleaned dataset
df.to_csv("../data/cleaned_rwanda_education_indicators.csv", index=False)

print("\nCleaned dataset saved to data/cleaned_rwanda_education_indicators.csv")
