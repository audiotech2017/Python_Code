# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    nums = [1, 2, 3, 4, 5]  #list
    array1 = np.array(nums)  #transfer the list to array
    for item in array1:
        print(item)
    zero_array = np.zeros(5)
    one_array = np.ones(5)

    for item in zero_array:
        print(item)
    range_array = np.arange(1, 10, 2)
    print(range_array)
    print(range_array.size)
    print(range_array.dtype)
    print(range_array.ndim)
    random_array = np.random.randint(1, 100, 5)
    print(random_array)
    random_array1 = np.random.rand(3, 3)
    print(random_array1)
    str1 = "="
    print(str1 * 100)

    array1 = np.array([1, 2, 3, 4, 5])
    array2 = np.array([5, 6, 7, 8, 9])
    sum = array1 + array2
    print(sum)
    print(np.sum(array1 + array2))
    greater_than = array1 > 3
    print(greater_than)
    print(str1 * 100)

    array3 = np.array([10, 20, 30, 40, 50])
    print(array3[1])  #the second data
    print(array3[-2])  #the last second data
    print(array3[1:4])  #the last second data
    print(array3[::2])  #the every second element

    matrix = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
    element = matrix[1, 1]  #single element
    elementrow = matrix[1, :]  #second row

    data = np.array([1, 2, 3, np.nan, 4, 5, 6])
    data_fill = np.nan_to_num(data, nan=999)
    print(data_fill)

    array4=np.array([[1,2],[3,4]])
    array5=np.array(([5,6],[7,8]))
    print(np.dot(array4,array5))

    array6=np.array([1,2,3,4,5,6])
    print(np.mean(array6))
    print(np.std(array6))
    np.savetxt('06output.csv',array5,delimiter=',')
    np.save('06outputmatrix.npy',matrix)
    new_matrix = np.load('06outputmatrix.npy')
    print(new_matrix)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
