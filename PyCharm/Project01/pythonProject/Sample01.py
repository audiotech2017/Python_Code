# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def lesson1():
    NAMES = ["John","Paul","George","Ringo"]
    AGES = [20,21,22,23]
    JOHN = NAMES[0]
    PAUL = NAMES[1]
    JOHN_PAUL = NAMES[:2]
    GEORGE_RINGO = NAMES[2:]
    REVERSE = NAMES[::-1]
    EVERY_OTHER = NAMES[::2]
    print(sum(AGES))
    print(min(AGES))
    print(max(AGES))
    print(JOHN_PAUL)
    print(GEORGE_RINGO)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    lesson1()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
