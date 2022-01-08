def recur(n, k):
    if n == 0 and k == 0:
        print("0")
        return
    if n < 0:
        print("Only Positive & Zero Number ! ! !")
        return
    if n == 0:
        print("".zfill(k))
        return
    recur(n-1, k)
    s = bin(n).replace('0b', '')
    print(s.zfill(k))


ip = int(input("Enter Number : "))
recur(2**ip - 1, ip)
