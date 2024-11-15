from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('cleaned_sales_data.csv')

# Aggregate data
product_sales = df.groupby('Product')['Sales_Amount'].sum().reset_index()
daily_sales = df.groupby('Date')['Sales_Amount'].sum().reset_index()

# Create figures
fig_product = px.bar(product_sales, x='Product', y='Sales_Amount', title='Sales by Product')
fig_daily = px.line(daily_sales, x='Date', y='Sales_Amount', title='Daily Sales Trend')

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1('Sales Dashboard'),
    dcc.Graph(figure=fig_product),
    dcc.Graph(figure=fig_daily)
])

if __name__ == '__main__':
    app.run_server(debug=True)
