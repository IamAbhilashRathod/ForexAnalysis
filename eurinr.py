import pandas as pd

# Studying EURINR pair in the file named 'eur_inr_data.csv' with columns 'Date' and 'EURINR' by naming it data in Python
data = pd.read_csv('eur_inr_data.csv')

# Creating a 'eur_inr_values' by taking EURINR values from the column 'EURINR'
eur_inr_values = data['EURINR']

# Seeing the max,min and average values
max_value = eur_inr_values.max()
min_value = eur_inr_values.min()
average_value = eur_inr_values.mean()

print("Highest:", max_value)
print("Lowest:", min_value)
print("Average:", average_value)

