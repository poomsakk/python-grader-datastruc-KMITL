def print_row(num, sharps):
    print('_'*(num-sharps), end="")
    print('#'*(sharps), end="")
    print()


def staircase(num, row=0):
    if num == 0:
        print('Not Draw!')
    elif num > 0:
        if row < num:
            row += 1
            print_row(num, row)
            staircase(num, row)
    else:
        if row < abs(num):
            print_row(abs(num), abs(num)-row)
            row += 1
            staircase(num, row)


staircase(int(input("Enter Input : ")))
