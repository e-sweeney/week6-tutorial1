import pandas as pd

# Load CSV file
df = pd.read_csv('data.csv')

# Show original data
print("Original Data:")
print(df.head())

# Strip whitespace from column names
df.columns = df.columns.str.strip()

# Remove leading/trailing whitespace from string values
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

# Convert string columns to lowercase
df = df.map(lambda x: x.lower() if isinstance(x, str) else x)

# Drop rows with any missing values
df.dropna(inplace=True)

# Drop duplicate rows
df.drop_duplicates(inplace=True)

# Save cleaned data
df.to_csv('cleaned_data.csv', index=False)

# Show original data
print("Cleaned Data:")
print(df.head())

print("\nCleaned data saved to 'cleaned_data.csv'")