import pandas as pd

# Load the sales data
df = pd.read_csv("data/raw/raw_sales_data.csv")  

# Show basic info
print(" Dataset Preview:")
print(df.head())

# Show column names and types
print("\nData Types:")
print(df.dtypes)

# Show missing values
print("\nMissing Values per Column:")
print(df.isna().sum())

#Checking for total rows
total_rows = df.shape[0]
print(f"\nTotal number of rows in the dataset: {total_rows}")

# Specifically checking Quantity
missing_qty = df['Quantity'].isna().sum()
print(f"\nMissing Quantity values: {missing_qty}")

