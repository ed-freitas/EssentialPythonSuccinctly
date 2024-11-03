# Importing Pandas
import pandas as pd

# Loading a CSV file
data = pd.read_csv('sample_data.csv')

# Displaying the first few rows of the dataset
print(data.head())

# Descriptive statistics
print(data.describe())

# Filtering data
filtered_data = data[data['column_name'] > 50]

# Aggregating data
grouped_data = data.groupby('category_column')['value_column'].mean()
print(grouped_data)
