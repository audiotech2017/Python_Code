import pandas as pd
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def find_sum(df):
    return df['price'].sum()


def find_sum_numpy(numbers: object):
    """

    :type numbers: numbers
    """
    array = np.array(numbers)
    return array.sum()


class BankAccount:
    def __init__(self, account_id, balance=1000):
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    data = {
        'order_id': [101, 102, 103, 104, 105],
        'price': [1000, 2000, 3000, 4000, 5000]
    }
    df = pd.DataFrame(data)
    print('the total price sum is: ', find_sum(df))
    numbers = [[7, 17], [13, 19], [5, 0]]
    print('the numpy total price sum is: ', find_sum_numpy(numbers))
    account1 = BankAccount('A12345')
    account1.deposit(1500)
    print(account1.get_balance())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
