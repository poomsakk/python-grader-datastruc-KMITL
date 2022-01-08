def weirdSubtract(n, k):
    while(k > 0):
        k -= 1
        if n % 10 == 0:
            n = int(n/10)
        else:
            n -= 1
    return n


n, s = input("Enter num and sub : ").split()
print(weirdSubtract(int(n), int(s)))
