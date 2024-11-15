import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv('cleaned_sales_data.csv')

# Prepare time series data
df['Date'] = pd.to_datetime(df['Date'])
daily_sales = df.groupby('Date')['Sales_Amount'].sum().reset_index()
daily_sales['Days'] = (daily_sales['Date'] - daily_sales['Date'].min()).dt.days

# Train a linear regression model
X = daily_sales[['Days']]
y = daily_sales['Sales_Amount']
model = LinearRegression()
model.fit(X, y)

# Predict future sales
future_days = pd.DataFrame({'Days': np.arange(daily_sales['Days'].max() + 1, daily_sales['Days'].max() + 31)})
future_sales = model.predict(future_days)

# Plot actual and forecasted sales
plt.plot(daily_sales['Days'], y, label='Actual Sales')
plt.plot(future_days['Days'], future_sales, label='Forecasted Sales', linestyle='--')
plt.legend()
plt.title('Sales Forecast')
plt.xlabel('Days')
plt.ylabel('Sales Amount')
plt.tight_layout()
plt.savefig('sales_forecast.png')
plt.show()
