
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import matplotlib.pyplot as plt


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    data = {'Date':['2024-01-01','2024-01-02','2024-01-03'],
            'Price':[123,234,345]
            }
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    df.plot(x='Date',y='Price', kind='line')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()

    data = {'Products':['A','B','C'],
            'Price':[123,234,345]
            }
    df = pd.DataFrame(data)
    df.plot(x='Products',y='Price', kind='bar')
    plt.xlabel('Products')
    plt.ylabel('Price')
    plt.show()
    df.to_csv('08outputcsv.csv')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

