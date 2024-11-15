import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv('cleaned_sales_data.csv')

# Group by product
product_sales = df.groupby('Product')['Sales_Amount'].sum()

# Visualize
product_sales.plot(kind='bar', title='Sales by Product', figsize=(8, 6))
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('sales_by_product.png')
plt.show()

# Sales trend over time
daily_sales = df.groupby('Date')['Sales_Amount'].sum()

# Plot time series
daily_sales.plot(title='Daily Sales Trend', figsize=(10, 6))
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('daily_sales_trend.png')
plt.show()
