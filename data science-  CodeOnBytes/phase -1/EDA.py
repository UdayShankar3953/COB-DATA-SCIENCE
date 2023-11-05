import pandas as pd

# Load the downloaded dataset
file_path = 'dataset - netflix1.csv'  # Replace with the actual file path
df = pd.read_csv(file_path)

# Display basic information about the dataset
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Handle missing values (example: replacing missing values in 'director' column with 'Unknown')
df['director'].fillna('Unknown', inplace=True)

# Convert date columns to datetime format
df['date_added'] = pd.to_datetime(df['date_added'])
df['release_year'] = pd.to_datetime(df['release_year'], format='%Y')  # Adjust format if needed

# Clean up 'duration' column (example: extract numeric values)
df['duration'] = df['duration'].str.extract('(\d+)').astype(float)  # Extracting numeric values

# Display the head of the cleaned dataset
print(df.head())

# Save the cleaned dataset to a new CSV file
df.to_csv('cleaned_data.csv', index=False)


# Display basic information about the dataset
print(df.info())

# Identify and remove outliers from the 'duration' column
column_name = 'duration'  # Replace with the column name containing outliers

# Calculate mean and standard deviation
mean = df[column_name].mean()
std_dev = df[column_name].std()

# Define a threshold (e.g., 3 standard deviations from the mean)
threshold = 3 * std_dev

# Filter out rows where the column value is considered an outlier
df = df[abs(df[column_name] - mean) < threshold]

# Display the head of the cleaned dataset after outlier removal
print(df.head())

# Save the cleaned dataset to a new CSV file
df.to_csv('cleaned_data_without_outliers.csv', index=False)

# outilers as been removed(8790-8781=9)
print(df.info())