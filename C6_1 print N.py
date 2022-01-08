def print1ToN(n):
    if n <= 1:
        print("1 ", end="")
        return
    print1ToN(n-1)
    print("{} ".format(n), end="")


def printNto1(n):
    n = 1 if n < 1 else n
    print("{} ".format(n), end="")
    if n <= 1:
        return
    else:
        printNto1(n-1)


n = int(input("Enter Input : "))

print1ToN(n)
printNto1(n)
