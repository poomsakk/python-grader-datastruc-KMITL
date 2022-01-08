def bubbleSort(arr):
    n = len(arr)
    negIndex = []
    for i in range(n):
        if arr[i] < 0:
            negIndex.append(i)

    negDataList = []
    maxIndex = n
    id = 0
    while id < maxIndex:
        if arr[id] < 0:
            negDataList.append(arr.pop(id))
            maxIndex -= 1
            continue
        id += 1

    for i in range(maxIndex-1):
        for j in range(0, maxIndex-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    for i in range(len(negIndex)):
        if arr == []:
            arr.append(negDataList[i])
        else:
            arr.insert(negIndex[i], negDataList[i])

    for i in arr:
        print(f"{i} ", end="")


arr = [int(x) for x in input("Enter Input : ").split()]
a = []
bubbleSort(arr)
