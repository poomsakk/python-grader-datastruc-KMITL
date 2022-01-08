def num_grid(lst):
    # trans '#' to int(0)
    for i in range(5):
        for j in range(5):
            if lst[i][j] != '#':
                lst[i][j] = 0
    for i in range(5):
        for j in range(5):
            if lst[i][j] == '#':
                # top-down
                if i == 0:
                    if lst[i+1][j] != '#':
                        lst[i+1][j] += 1
                elif i == 4:
                    if lst[i-1][j] != '#':
                        lst[i-1][j] += 1
                else:
                    if lst[i+1][j] != '#':
                        lst[i+1][j] += 1
                    if lst[i-1][j] != '#':
                        lst[i-1][j] += 1
                # left-right
                if j == 0:
                    if lst[i][j+1] != '#':
                        lst[i][j+1] += 1
                elif j == 4:
                    if lst[i][j-1] != '#':
                        lst[i][j-1] += 1
                else:
                    if lst[i][j+1] != '#':
                        lst[i][j+1] += 1
                    if lst[i][j-1] != '#':
                        lst[i][j-1] += 1
                # Down-Right
                if i < 4 and j < 4 and lst[i+1][j+1] != '#':
                    lst[i+1][j+1] += 1
                # Down-Left
                if i < 4 and j > 0 and lst[i+1][j-1] != '#':
                    lst[i+1][j-1] += 1
                # Top-Right
                if i > 0 and j < 4 and lst[i-1][j+1] != '#':
                    lst[i-1][j+1] += 1
                # Top-Left
                if i > 0 and j > 0 and lst[i-1][j-1] != '#':
                    lst[i-1][j-1] += 1
    # change to string
    for i in range(5):
        for j in range(5):
            if lst[i][j] != '#':
                lst[i][j] = str(lst[i][j])

    return lst


'''
lst_input = [
    ["-","-","-","-","-"],
    ["-","-","-","-","-"],
    ["-","-","#","-","-"],
    ["-","-","-","-","-"],
    ["-","-","-","-","-"]
]
'''
print("*** Minesweeper ***")
lst_input = []
input_list = input("Enter input(5x5) : ").split(",")
for e in input_list:
    lst_input.append([i for i in e.split()])
print("\n", *lst_input, sep="\n")
print("\n", *num_grid(lst_input), sep="\n")
