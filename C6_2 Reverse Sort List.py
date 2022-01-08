def backwards(lis):
    if len(lis) == 0:
        return []
    else:
        return backwards(lis[1:]) + lis[:1]



ip = [int(x) for x in input("Enter your List : ").split(",")]
print("List after Sorted : ", end="")
print(backwards(sorted(ip)))
