#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    temp = []
    for x in my_list:
        if x % 2 == 0:
            temp.append(True)
        else:
            temp.append(False)
    return temp
