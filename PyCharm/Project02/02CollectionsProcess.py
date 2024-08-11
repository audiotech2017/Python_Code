# This is a sample Python script.
from typing import List


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def prepare_list(animals):  # de-duplicate
    return sorted(set(animals))


def insert_item(my_tuple, new_value, index):
    return my_tuple[:index] + (new_value,) + my_tuple[index:]


def build_menu(p_cakes):
    p_cakes[105] = ["Coffee", 1.49]
    items = []
    for flavor, price in p_cakes.values():
        items.append(f"{flavor} Cake - ${price}")
    return list(reversed(sorted(items)))


def find_winner(player_score):
    highest_avg = 0
    highest_avg_player = ""
    for player, scores in player_score.items():
        avg = sum(scores) / len(scores)
        print(player, scores)
        if avg > highest_avg:
            highest_avg = avg
            highest_avg_player = player
    return [highest_avg_player, highest_avg]


def describe_items(food_items, color):
    result = []
    for food in food_items:
        print("food: ",food)
        for typex in food_items[food]:
            print("typex: ", typex)
            for itemx in food_items[food][typex]:
                print("itemx: ", itemx)
                if food_items[food][typex][itemx]['color'] == color:
                    result.append(f"The {itemx} is {food_items[food][typex][itemx]['taste']}.")
    return result


def read_file(text):
    with open('03outputexample.txt', 'w') as file:
        file.write(text+'1\n')
        file.write(text+'2\n')
        file.write(text+'3\n')
        file.close()
    with open('03outputexample.txt', 'r') as file:
        result: list[str] = []
        #result.append(file.readline()) # 这里还可以read() readlines() 当前使用的是一条一条读取
        #result.append(file.readline())
        #result.append(file.readline())
        #下面是第二种方法
        result: list[str] = [file.readline(), file.readline(), file.readline()]
        file.close() # 关闭文件
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    animals = ["crow", "cat", "dog", "woodpecker", "fox", "fox", "crow", "dog", ]
    print("Set Function with Sort set data: ", prepare_list(animals))
    print("Simple Set Function set data: ", set(animals))
    print("List data: ", animals)

    sports = ('football', 'basketball', 'cricket', 'hokey', 'tennis', 'volleyball')
    new_value1 = 'baseball'
    index1 = 2
    print("insert into tuple1: ", insert_item(sports, new_value1, index1))
    numbers = (7, 17, 13, 19, 5)
    new_value2 = 11
    index2 = 3
    print("insert into tuple2: ", insert_item(numbers, new_value2, index2))
    cakes = {
        100: ["Carrot", 1.99],
        101: ["Chocolate", 1.99],
        102: ["Strawberry", 2.99],
        103: ["Spice", 2.79],
        104: ["Vanilla", 1.79]
    }
    print("build menu insert coffee list: ", build_menu(cakes))
    player_scores = {
        'Arthur': [83, 90, 92],
        'Bela': [85, 90, 97],
        'Carol': [85, 55, 92],
        'Deepak': [85, 78, 92],
        'Eric': [85, 90, 99],
    }
    print("The Winner is: ", find_winner(player_scores))
    food_items = {
        'fruits': {
            'tropical': {
                'mango': {
                    'color': 'orange',
                    'taste': 'sweet',
                    'nutrients': ['vitamin C', 'vitamin A', 'fiber']
                },
                'pineapple': {
                    'color': 'yellow',
                    'taste': 'tangy',
                    'nutrients': ['vitamin C', 'manganese', 'fiber']
                },
                'temperate': {
                    'color': 'red',
                    'taste': 'sweet',
                    'nutrients': ['vitamin C', 'potassium', 'fiber']
                },
                'beet': {
                    'color': 'red',
                    'taste': 'earthy',
                    'nutrients': ['vitamin C', 'floate', 'iron']
                }
            }
        }
    }
    print('describe the food items: ', describe_items(food_items, 'yellow'))
    print('describe the food items: ', describe_items(food_items, 'red'))
    print('write output and read as input: ',read_file('hello'))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
