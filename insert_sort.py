# encoding: utf-8

"""
date: 2020/05/30/00/05

"""

def insert_sort(list):

    for j in range(1, len(list)):
        key = list[j]
        i = j - 1
        while i >= 0 and list[i] > key:
            list[i+1] = list[i]
            i = i - 1
        list[i+1] = key

    return list


list = [5, 2, 4, 6, 1, 3]

if __name__ == '__main__':
    print(insert_sort(list))
