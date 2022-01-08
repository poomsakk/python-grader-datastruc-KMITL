def findMin(lst, min=9999999999):
    if lst == []:
        return min
    else:
        if lst[len(lst)-1] < min:
            min = lst[len(lst)-1]
        lst.pop()
        return findMin(lst, min)


ip = [int(x) for x in input("Enter Input : ").split()]
print("Min :", findMin(ip))
