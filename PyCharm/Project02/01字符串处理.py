# This is a sample Python script.
from string import ascii_lowercase


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def check_strings(first_string, second_string):
    return first_string == second_string


def replace_string(orig_string, old_string, new_string):
    return orig_string.replace(old_string, new_string)


def reverse_string(orig_string):
    return orig_string[::-1]


def add_product_code(product_code, product_id):
    str = product_id[4:9]
    if product_id[4:9] == product_code:
        return product_id
    else:
        return product_id[:4] + product_code + product_id[4:]


def add_product_code1(product_code, product_id):
    if product_id[4:9] == product_code:
        return product_id
    else:
        first_string = product_id[:4]
        second_string = product_id[4:]
        return f'{first_string}{product_code}{second_string}'  #格式化输出


def check_string(input_string):
    missing = ""
    for i in ascii_lowercase:
        if i not in input_string.lower():
            missing += i  #将missing的字符串联起来 print(i) #debug print for more informaiton
    if len(missing) > 0:
        return f"the string missing following letters: {missing}"
    else:
        return f"the string contains all the letters of the alphabet."


def is_anagram(first_str, second_str):
    letters1 = ""
    letters2 = ""
    for letter in first_str.lower():
        letters1 += letter if letter.isalpha() else ""
    for letter in second_str.lower():
        letters2 += letter if letter.isalpha() else ""
    print(sorted(letters1))
    print(sorted(letters2))
    return sorted(letters1) == sorted(letters2)


if __name__ == '__main__':
    print_hi('PyCharm')
    print(check_strings('abc', 'abc'))
    print(replace_string('abide', 'a', 'b'))

    mystring = 'hello world'
    print('打印2-8序列 间隔为1: ' + mystring[1:8:1])
    print('打印2-8序列 间隔为2: ' + mystring[1:8:2])  #第二个开始打印8个序列 其中间隔为2
    print('打印所有序列 逆序排列: ' + mystring[::-1])
    print('打印所有序列 逆序排列: ' + reverse_string(mystring))  #这里为逆序排列
    mynum1 = 123.456
    mynum2 = 234.789
    total = mynum1 + mynum2
    print(f"{mynum1} plus {mynum2} equal to {total}")  #这里是单独相加
    print(f"{mynum1} plus {mynum2} equal to {mynum1 + mynum2}")  #这里是直接相加
    print(mystring[:3] + "123123" + mystring[3:])  #插入字符串
    product_code1 = "09283"
    product_id1 = "btc--blk-3ghz"
    product_code2 = "36629"
    product_id2 = "kit-36629-blk-3ghz"
    print('orig product id: ' + product_id1 + ' new product id: ' + add_product_code(product_code1,
                                                                                     product_id1))  # product_id会有变化
    print('orig product id: ' + product_id2 + ' new product id: ' + add_product_code(product_code2,
                                                                                     product_id2))  # product_id没有变化
    print(add_product_code1(product_code1, product_id1))
    print(add_product_code1(product_code2, product_id2))

    str1 = "How quickly jumping zebras."
    str2 = "Sphinx of black quartz, judge my vow."
    print(check_string(str1))
    print(check_string(str2))

    str1 = "Eleven plus two?"
    str2 = "One plus twelve!"
    str3 = "A cinnamon roll?"
    str4 = "No canola oil, Mr.!"

    print(is_anagram(str1, str2))
    print(is_anagram(str3, str4))
    print(sorted('cat'))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
