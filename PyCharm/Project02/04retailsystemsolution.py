# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import matplotlib.pyplot as plt


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class RetailSalesAnalyzer:
    def __init__(self):
        self.data = pd.read_csv('04retail_sales.csv')
        print(self.data)
        self.data.dropna(inplace=True)
        self.data['Date'] = pd.to_datetime(self.data['Date'],format='%Y/%m/%d',errors='ignore')
        print(self.data)

    def total_sales_per_product(self):
        return self.data.groupby('Product')['Sales'].sum()

    def best_selling_product(self):
        return self.total_sales_per_product().sort_values(ascending=False).index[0]

    def average_daily_sales(self):
        return self.data['Sales'].mean()


    def plot_sales_trend(self):
        self.data.groupby('Date')['Sales'].sum().plot(kind='line')
        plt.title('Sales Trend over Time')
        plt.xlabel('Date')
        plt.ylabel('Total Sales')
        plt.show()

    def plot_sales_per_product(self):
        self.total_sales_per_product().plot(kind='bar')
        plt.title('Sales Per Product')
        plt.xlabel('Product')
        plt.ylabel('Total Sales')
        plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    analyze = RetailSalesAnalyzer()
    #analyze.data_clean()
    print('Total sales Per Product: \n', analyze.total_sales_per_product())
    print('Best selling Product: \n', analyze.best_selling_product())
    print('Average Daily Sales: \n', analyze.average_daily_sales())
    analyze.plot_sales_trend()
    analyze.plot_sales_per_product()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
