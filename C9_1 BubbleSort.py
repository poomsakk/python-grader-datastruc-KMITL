def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
        swap = False
        move = None

        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                move = arr[j]
                swap = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if i == n-2:
            print(f"last step : {arr} move[{move}]")
        elif swap:
            print(f"{i+1} step : {arr} move[{move}]")


arr = [int(x) for x in input("Enter Input : ").split()]

bubbleSort(arr)
