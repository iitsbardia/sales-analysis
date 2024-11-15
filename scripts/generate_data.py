import pandas as pd
import numpy as np
import random

# Generate synthetic data
np.random.seed(42)

dates = pd.date_range(start='2021-01-01', end='2023-01-01', freq='D')
products = ['Product A', 'Product B', 'Product C', 'Product D']
regions = ['North', 'South', 'East', 'West']

data = {
    'Date': np.random.choice(dates, size=1000),
    'Product': np.random.choice(products, size=1000),
    'Region': np.random.choice(regions, size=1000),
    'Sales_Amount': np.random.uniform(50, 500, size=1000),
    'Discount': np.random.uniform(0, 0.3, size=1000)
}

df = pd.DataFrame(data)

# Introduce some missing values and outliers for cleaning
df.loc[random.sample(range(len(df)), 20), 'Sales_Amount'] = np.nan
df.loc[random.sample(range(len(df)), 5), 'Sales_Amount'] = 10000

# Save dataset
df.to_csv('synthetic_sales_data.csv', index=False)
print("Dataset generated as synthetic_sales_data.csv")
