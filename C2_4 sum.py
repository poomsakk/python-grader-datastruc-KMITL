import sys
input = [x for x in input("Enter Your List : ").split()]
lens = len(input)
if lens < 3:
    print("Array Input Length Must More Than 2")
    sys.exit(0)
ans = []
Bool = True
while(Bool):
    b = False
    Bool = False
    lens = len(input)
    for i in range(lens):
        for j in range(lens):
            for k in range(lens):
                if i != j and j != k and i != k:
                    if int(input[i])+int(input[j])+int(input[k]) == 0:
                        aa = input[i]
                        bb = input[j]
                        cc = input[k]
                        if [int(input[i]), int(input[j]), int(input[k])] not in ans:
                            ans.append(
                                [int(input[i]), int(input[j]), int(input[k])])
                        input.remove(aa)
                        input.remove(bb)
                        input.remove(cc)
                        b = True
                        Bool = True
                        break
            if b:
                break
        if b:
            break
print(ans)
