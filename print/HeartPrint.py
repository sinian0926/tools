def print_heart():
    # 行长度
    line = 31
    up_height = 3
    down_height = 8
    mid = line // 2

    # 上半部分
    for i in range(up_height):
        for j in range(line):
            # 空格下标
            space_num = (up_height - (i + 1)) * 2

            if space_num - 1 < j < mid - space_num or mid + space_num < j < line - space_num:
                print('*', end='')
            elif j < 21:  # line - space_num
                print(' ', end='')

        # 换行
        print()

    # 下半部分
    for i in range(down_height):
        for j in range(line):
            # 空格下标
            space_num = (i + 1) * 2

            if space_num - 2 < j < line - space_num + 1:
                print('*', end='')
            else:
                print(' ', end='')

        # 换行
        print()


if __name__ == '__main__':
    print_heart()
