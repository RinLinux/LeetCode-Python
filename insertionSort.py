

def insertion_sort(num:list):
    n = len(num)
    if n <= 1:
        return num

    for i in range(1, n):
        key = num[i]
        j = i - 1
        while j >=0 and num[j] > key:
            num[j + 1] = num[j]
            j -= 1
        num[j + 1] = key
        
    return num

if __name__ == '__main__':
    num = [6, 4, 5, 1, 2, 3]
    print(insertion_sort(num))