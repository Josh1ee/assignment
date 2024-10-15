import pandas as pd

# Corrected file path - using raw string (Option 1)
file_path = r'C:\Users\Josh\Documents\FIT3179\A2\data\malaysia_forest_deforestation.csv'

# Alternatively, use forward slashes (Option 2)
# file_path = 'C:/Users/Josh/Documents/FIT3179/A2/data/malaysia_forest_deforestation.csv'

# Load the CSV file
df = pd.read_csv(file_path)

# Get the unique state names
unique_states = df['state'].unique().tolist()

# Print the unique states
print(unique_states)
