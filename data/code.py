import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv('data/combined_deforestation_flood.csv')

# Convert YEAR to integer, replacing NaN with a placeholder value
df['YEAR'] = pd.to_numeric(df['YEAR'], errors='coerce').fillna(0).astype(int)

# Ensure numerical columns are float
numerical_columns = ['forest_cover_percentage', 'deforestation_rate', 'flood_occurrences', 'TOTAL_RAINFALL', 'ANNUAL RAINFALL']
for col in numerical_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Convert boolean column to lowercase string
df['has_flood_data'] = df['has_flood_data'].astype(str).str.lower()

# Remove rows with missing values in critical columns
critical_columns = ['YEAR', 'STATE', 'deforestation_rate', 'flood_occurrences', 'TOTAL_RAINFALL']
df = df.dropna(subset=critical_columns)

# Print summary statistics
print(df.describe())

# Print unique values in categorical columns
print("\nUnique values in STATE column:")
print(df['STATE'].unique())

print("\nUnique values in has_flood_data column:")
print(df['has_flood_data'].unique())

# Print rows where YEAR is 0 (was originally NaN)
print("\nRows with YEAR as 0 (originally NaN):")
print(df[df['YEAR'] == 0])

# Save the cleaned CSV
df.to_csv('data/cleaned_combined_deforestation_flood.csv', index=False)

print("\nCleaned CSV saved. Row count:", len(df))

# Additional data quality checks
print("\nColumn-wise null count:")
print(df.isnull().sum())

print("\nData types of columns:")
print(df.dtypes)

print("\nValue ranges for numerical columns:")
for col in numerical_columns + ['YEAR']:
    print(f"{col}: {df[col].min()} to {df[col].max()}")