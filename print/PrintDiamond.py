def print_diamond(r):
    d = 2 * r
    index = 0
    for i in range(r):
        for j in range(d):
            if r - i <= j <= r + i:
                print('*', end='')
            elif j < r + i:
                print(' ', end='')
        index += 1
        print(index)

    for i in range(r - 1):
        for j in range(d):
            # if j < i + 2 or j > r - i + 1 :
            if i + 2 <= j <= d - (i + 2):
                print('*', end='')
            elif j < d - (i + 2):
                print(' ', end='')
        index -= 1
        print(index)


if __name__ == '__main__':
    print_diamond(4)
