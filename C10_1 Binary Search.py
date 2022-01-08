def bi_search(l, r, arr, x):
    if l > r:   # base case
        return False

    mid = (l+r)//2      # find middle of array

    if x == arr[mid]:             # check middle itself
        return True
    elif x < arr[mid]:                             # if x is less than middle
        return bi_search(l, mid-1, arr, x)        # recursive left side
    elif x > arr[mid]:                             # if x is more than middle
        return bi_search(mid+1, r, arr, x)    # recursive right side


inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))
