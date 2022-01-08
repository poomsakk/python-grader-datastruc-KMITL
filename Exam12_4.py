n = int(input("Enter a positive number : "))
if n < 0:
    print("{} is too low.".format(n))
    quit()
elif n >= 16:
    print("{} is too high.".format(n))
    quit()
# top
for i in range(1, n+1):
    print("%X " % (i), end="")
print()
# middle
for i in range(2, n):
    print("%X " % (i), end="")
    for j in range(2, n):
        print("  ", end="")
    print("%X " % (i-1), end="")
    print()
# bottom
print("%X " % (n), end="")
for i in range(1, n):
    print("%X " % (i), end="")
print()
