import pandas as pd
# Creating the DataFrame
sales_data = {
    'Product': ['A', 'B', 'C', 'A', 'B', 'C'], 
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], 
    'Amount': [150, 220, 180, 200, 250, 210]
}
sales_data = pd.DataFrame(sales_data)
print("# Creating the DataFrame")
print(sales_data)

# Display the first 3 rows of the DataFrame
print("Display the first 3 rows of the DataFrame")
sales_data_subset = sales_data.head(3)
print(sales_data_subset)

# Display the 'Product' column for all rows
print("Display the 'Product' column for all rows")
print(sales_data['Product'])

# Display the sales data for the month of 'May'
may_sales = sales_data[sales_data['Month'] == 'May']
print("Display the sales data for the month of 'May'")
print(may_sales)

# Display sales data for the products 'A' and 'C'
filtered_products = sales_data[sales_data['Product'].isin(['A', 'C'])]
print("Display sales data for the products 'A' and 'C'")
print(filtered_products)

# Display the sales data where the amount is greater than 200
high_sales = sales_data[sales_data['Amount'] > 200]
print("Sales data with amount greater than 200:")
print(high_sales)