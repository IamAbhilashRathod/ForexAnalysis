import pandas as pd

# Studying GBPINR pair from csv file named "gbp_inr_data.csv"  with columns 'date' and 'GBPINR' by naming it data in Python
data = pd.read_csv('gbp_inr_data.csv')

# Taking GBPINR values
gbp_inr_values = data['GBPINR']

# Seeing the max, min and average values of the pair btwn 01Jan20 to 16Mar24
max_value = gbp_inr_values.max()
min_value = gbp_inr_values.min()
average_value = gbp_inr_values.mean()

print("Highest:", max_value)
print("Lowest:", min_value)
print("Average:", average_value)

