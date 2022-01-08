count = 0


def shellSort(array, n):
    interval = 8 // 2
    global count
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            count += 1
            while j >= interval and array[j - interval] > temp:
                count += 1
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2
    return count


print("  Shell sort ")
array = list(map(int, input("Enter some numbers : ").split()))
size = len(array)
round = shellSort(array, size)
print()
print(array)
print("Data comparison =  {}".format(round))
