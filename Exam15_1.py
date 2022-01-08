def natural_sum(n):
    if n == 1:
        return 1
    else:
        return n + natural_sum(n-1)


def print1ToN(base, n):
    if base == n == 1:
        print("1 = ", end="")
        return
    if n <= 1:
        print("1 + ", end="")
        return
    print1ToN(base, n-1)
    print("{} ".format(n), end="")
    if n == base:
        print("= ".format(n), end="")
    else:
        print("+ ".format(n), end="")


print(" *** Natural sum ***")
num = int(input("Enter number : "))
print1ToN(num, num)
print("%.d" % (natural_sum(num)))
