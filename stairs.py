
def stairs(n):
    if n <= 2:
        return n
    return stairs(n-1) + stairs(n-2)

def stairs_nr(n):
    if n <= 2:
        return n

    prev_prev = 1
    prev = 2
    all_step = 0

    for i in range(2, n, 1):
        all_step = prev_prev + prev
        prev_prev, prev = prev, all_step
    
    return all_step

    
    
if __name__ == '__main__':
    print(stairs(15))
    print(stairs_nr(1000))