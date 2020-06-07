# encoding: utf-8

"""
date: 2020/03/06/17/10

"""
def value(m:"数独矩阵", x:"空白格行数", y:"空白格列数"):
    """ 功能：返回符合"每个横排和竖排以及
              九宫格内无相同数字"这个条件的有效值。
    """
    i, j = x//3, y//3
    grid = [m[i*3+r][j*3+c] for r in range(3) for c in range(3)]
    # print(grid)
    # print(set(grid))
    # print(m[0])
    # print((list(zip(*m))[0]))
    v = set([x for x in range(1,10)]) - set(grid) - set(m[x]) - set(list(zip(*m))[y])
    return list(v)

if __name__ == '__main__':
    m = [
            [6, 0, 0, 1, 0, 0, 7, 0, 8],
            [0, 0, 0, 8, 0, 0, 2, 0, 0],
            [2, 3, 8, 0, 5, 0, 1, 0, 0],
            [0, 0, 0, 0, 4, 0, 0, 9, 2],
            [0, 0, 4, 3, 0, 8, 6, 0, 0],
            [3, 7, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 3, 0, 7, 0, 5, 2, 6],
            [0, 0, 2, 0, 0, 4, 0, 0, 0],
            [9, 0, 7, 0, 0, 6, 0, 0, 4]
        ]
    print(value(m, 0, 1))