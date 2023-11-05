import pandas as pd

# Load the downloaded dataset
file_path = 'dataset - netflix1.csv'  # Replace with the actual file path
df = pd.read_csv(file_path)

# Display basic information about the dataset
print(df.info())

# Example visualizations
# Plotting count of 'type' (Movie vs TV Show)
sns.countplot(x='type', data=df)
plt.title('Count of Movies and TV Shows')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()


# Creating a histogram of 'release_year'
sns.histplot(data=df, x='release_year', bins=20, kde=True)
plt.title('Distribution of Release Years')
plt.xlabel('Release Year')
plt.ylabel('Frequency')
plt.show()


# Create a boxplot for 'duration' to detect outliers
sns.boxplot(data=df, y='duration')
plt.title('Boxplot of Duration')
plt.ylabel('Duration')
plt.show()


# Drop non-numeric or irrelevant columns for correlation
non_numeric_cols = ['show_id']  # Adjust with other non-numeric columns if needed
df_numeric = df.select_dtypes(include=['int64', 'float64'])

# Display basic information about the remaining numeric columns
print(df_numeric.info())

# Correlation matrix heatmap for numeric columns
sns.heatmap(df_numeric.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix Heatmap')
plt.show()

