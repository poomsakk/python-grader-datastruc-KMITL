ip = [int(x) for x in input("Enter number end with (-1) : ").split()]
if not -1 in ip:
    print("Invalid INPUT !!!")
    quit()
num = []
for i in ip:
    if i == -1:
        break
    else:
        num.append(i)
half = len(num)/2

for i in num:
    if num.count(i) > half:
        print(i)
        quit()
print("Not found")
