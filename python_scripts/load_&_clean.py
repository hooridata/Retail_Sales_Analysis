import pandas as pd
import os

# Define path
input_path = os.path.join('data', 'raw', 'raw_sales_data.csv')
output_path = os.path.join('data', 'cleaned', 'sales_data_cleaned.csv')

# Step 1: Load the raw CSV
df = pd.read_csv(input_path)

# Step 2: Drop rows with missing 'Product'
df = df.dropna(subset=['Product'])

# Step 3: Fill missing 'Quantity' with mean per Product
df['Quantity'] = df.groupby('Product')['Quantity'].transform(
    lambda x: x.fillna(x.mean())
)

# Step 4: Save the cleaned data
df.to_csv(output_path, index=False)

print("✅ Cleaned data saved to:", output_path)
