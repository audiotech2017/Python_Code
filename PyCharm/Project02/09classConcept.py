# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        return f"{self.name} is a {self.position} with salary as of {self.salary}"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    employee1 = Employee('Eric', 'Finance Head', '123456')
    employee2 = Employee('Jack', 'Human Resource Head', '234567')
    print(employee1.display_info())
    print(employee2.display_info())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
