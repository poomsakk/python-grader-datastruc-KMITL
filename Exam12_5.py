class MyInt:
    def __init__(self, n):
        self.n = n

    def isPrime(self):
        num = self.n
        if num < 2:
            return False
        for i in range(2, num//2):
            if num % i == 0:
                return False
        return True

    def showPrime(self):
        num = self.n
        if num < 2:
            return "!!!A prime number is a natural number greater than 1"
        s = ""
        for i in range(2, num+1):
            isPime = True
            for j in range(2, i):
                if i % j == 0:
                    isPime = False
                    break
            if isPime:
                s = s + "{} ".format(i)
        return s

    def __sub__(self, other):
        return self.n - other.n//2


print(" *** class MyInt ***")
x, y = [int(i) for i in input("Enter 2 number : ").split()]
a = MyInt(x)
b = MyInt(y)
print("{} isPrime : {}".format(x, a.isPrime()))
print("{} isPrime : {}".format(y, b.isPrime()))
print("Prime number between 2 and {} : {}".format(x, a.showPrime()))
print("Prime number between 2 and {} : {}".format(y, b.showPrime()))
print("{} - {} = {}".format(x, y, a-b))
