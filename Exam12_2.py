print(" *** Perfect Number Verification ***")
num = int(input("Enter number : "))
if num < 0:
    print("Only positive number !!!")
    quit()
factors = []
sum = 0
for i in range(1, num):
    if num % i == 0:
        factors.append(i)
        sum += i
if num == sum:
    print("{} is a PERFECT NUMBER.".format(num))
else:
    print("{} is NOT a perfect number.".format(num))
print("Factors : ", end="")
print(factors)
