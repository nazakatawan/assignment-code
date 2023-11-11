import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.ticker import ScalarFormatter

file_name = 'Superstore Sales.csv'
df= pd.read_csv(file_name,encoding='latin-1')
print(df)



'''def sales_line_chart(data, year_col='Year', region_col='Region', sales_col='Sales'):
    data[year_col] = data[year_col].astype(int)
    grouped_data = data.groupby([year_col, region_col])[sales_col].sum().unstack()

    # Plotting the line chart
    plt.figure(figsize=(10, 6))

    for region in grouped_data.columns:
        plt.plot(grouped_data.index, grouped_data[region], label=region)

    plt.title('Sales by Region Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Sales')
    plt.legend()
    plt.xticks(grouped_data.index)
    plt.grid(True)
    plt.show()


sales_line_chart(df)'''



'''def top5products(data, product_col='Product Name', quantity_col='Quantity'):

    # Grouping data by 'Product Name' and summing up the quantity
    product_quantity = data.groupby(product_col)[quantity_col].sum()

    # Selecting the top 5 products
    top5_products = product_quantity.nlargest(5)

    # Plotting the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(top5_products, labels=top5_products.index, autopct='%1.1f%%', startangle=140)
    plt.title('Top 5 Products by Quantity')
    plt.show()

top5products(df)'''


'''def profit_bar_chart(data, category_col='Category', profit_col='Profit'):


    category_profit = data.groupby(category_col)[profit_col].sum()

    # Define colors for each category
    colors = ['skyblue', 'lightcoral', 'lightgreen']

    # Plotting the bar chart with colors and legend
    plt.figure(figsize=(10, 6))
    category_profit.sort_values().plot(kind='barh', color=colors)
    plt.title('Profit Distribution by Category')
    plt.xlabel('Profit')
    plt.ylabel('Category')
    plt.legend(category_profit.index, loc='lower right')  # Add legend with category names
    plt.show()

profit_bar_chart(df)'''

'''Region wise sales comparison using line chart, top 5 products in terms of quantity 
Visualization of profitable category of 
products'''







