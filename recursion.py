# encoding: utf-8

"""
date: 2020/03/08/12/49

"""

def product_multiply(x, y):
    if y == 0:
        return 0
    else:
        return x + product_multiply(x, y-1)



if __name__ == '__main__':
    print(product_multiply(5,3))