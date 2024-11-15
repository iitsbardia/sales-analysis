import pandas as pd

# Load data
df = pd.read_csv('synthetic_sales_data.csv')

# Handle missing values
df['Sales_Amount'].fillna(df['Sales_Amount'].median(), inplace=True)

# Remove outliers (values beyond 99th percentile)
upper_limit = df['Sales_Amount'].quantile(0.99)
df = df[df['Sales_Amount'] <= upper_limit]

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Save cleaned dataset
df.to_csv('cleaned_sales_data.csv', index=False)
print("Cleaned data saved as cleaned_sales_data.csv")
