import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned data
df = pd.read_csv("data/cleaned/sales_data_cleaned.csv")

# Basic info
print("Data Shape:", df.shape)
print("\nColumn Names:", df.columns.tolist())
print("\nData Types:\n", df.dtypes)
print("\nNull Values:\n", df.isna().sum())

# Convert OrderDate to datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# 1. Top 10 most sold products
top_products = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Most Sold Products:\n", top_products)

# 2. Sales trend over time
daily_sales = df.groupby('OrderDate')['Quantity'].sum()
daily_sales.plot(figsize=(12,6), title='Daily Sales Quantity Over Time')
plt.xlabel('Date')
plt.ylabel('Quantity Sold')
plt.tight_layout()
plt.show()

# 3. Total revenue per product
df['Revenue'] = df['Quantity'] * df['Price']
product_revenue = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Revenue-Generating Products:\n", product_revenue)

# 4. Sales by day of the week
df['Weekday'] = df['OrderDate'].dt.day_name()
weekday_sales = df.groupby('Weekday')['Quantity'].sum().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])
weekday_sales.plot(kind='bar', title='Sales by Weekday', figsize=(10,5))
plt.ylabel('Quantity Sold')
plt.tight_layout()
plt.show()

# 5. Distribution of Quantity
plt.figure(figsize=(8,5))
sns.histplot(df['Quantity'], bins=30, kde=True)
plt.title('Distribution of Quantity Sold')
plt.tight_layout()
plt.show()
