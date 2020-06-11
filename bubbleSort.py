

def bubble_sort(num:list):
    n = len(num)
    if n <=1 :
        return num

    for i in range(0, n):
        trs = False
        for j in range(0, n - i -1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
            trs = True

        if (not trs):
            break


    return num


if __name__ == '__main__':
    num = [4, 5, 6, 1, 2, 3]
    print(bubble_sort(num))