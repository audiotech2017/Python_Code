# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    print(df.columns)
    df = pd.read_csv('07SharepointLogs.csv')
    print(df.columns)
    #print(df.to_string()) # print all the csv data
    new_df = df.dropna()  # clean na data
    new_df = df.fillna(100, inplace=True)
    new_df = df.drop_duplicates()
    #print(new_df)
    print((df.groupby("Category")["Category"].count()))
    #print(df.aggregate(['sum','min']))

    df1 = pd.read_json('07SampleJson.json')
    print(df1.to_string())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
