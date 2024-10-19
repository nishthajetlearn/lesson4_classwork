import pandas as pd

# Loading the data from a file (titanic.csv)
data = pd.read_csv("titanic.csv")

# This would return rows where both conditions are met (i.e., Age > 20 and Pclass is 1).
filtered_data = data[(data['Age'] > 20) & (data['Pclass'] == 1)]
print("Filtered data where Age > 20 and Pclass is 1:")
print(filtered_data.head())  # Using .head() to limit the number of rows shown

# If we want to filter people who are either older than 30 or belong to the 3rd class (Pclass == 3):
filtered_data = data[(data['Age'] > 30) | (data['Pclass'] == 3)]
print("Filtered data where Age > 30 or Pclass is 3:")
print(filtered_data.head())

# Sorting by 'Age'
sorted_df = data.sort_values(by='Age')
print("Data sorted by Age:")
print(sorted_df.head())

# Sorting by multiple columns ('Pclass' then 'Age')
sorted_df_multiple = data.sort_values(by=['Pclass', 'Age'])
print("Data sorted by Pclass then Age:")
print(sorted_df_multiple.head())

# Adding a new column 'Age_in_10_years', showing age after 10 years
data['Age_in_10_years'] = data['Age'] + 10
print("Data with a new column 'Age_in_10_years':")
print(data[['Name', 'Age', 'Age_in_10_years']].head())

# Adding a new column 'Is_Adult', which is True if Age >= 18
data['Is_Adult'] = data['Age'] >= 18
print("Data with a new column 'Is_Adult':")
print(data[['Name', 'Age', 'Is_Adult']].head())
