import pandas as pd

# Reading data of the USDINR pair in a CSV file named 'usd_inr_data.csv' with columns 'Date' and 'USDINR'
data = pd.read_csv('usd_inr_data.csv')

# Extracting USDINR values
usd_inr_values = data['USDINR']

# Calculating max, min, and average
max_value = usd_inr_values.max()
min_value = usd_inr_values.min()
average_value = usd_inr_values.mean()

print("Maximum value:", max_value)
print("Minimum value:", min_value)
print("Average value:", average_value)


