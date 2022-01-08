print("*** Fun with countdown ***")
input = [int(x) for x in input("Enter List : ").split()]
lens = len(input)
count = 0
li = []
curr = []
for i in range(lens):
    if input[i] == 1:
        curr.append(input[i])
        li.append([x for x in curr])
        curr.clear()
        count += 1
        continue
    if input[i] == input[i-1] - 1:
        curr.append(input[i])
        continue
    else:
        curr.clear()
        curr.append(input[i])
print([count, li])
