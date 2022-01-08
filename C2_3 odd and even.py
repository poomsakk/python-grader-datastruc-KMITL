def odd_even(arr, s):
    List = s.split(",")
    if arr == 'S':
        s = ""
        List[0] = List[0].replace(" ", "")
        for i in range(len(List[0])):
            if List[1] == "Even" and i % 2 == 1:
                s += List[0][i]
            elif List[1] == "Odd" and i % 2 == 0:
                s += List[0][i]
        return s
    elif arr == 'L':
        l = []
        List[0] = List[0].split()
        for i in range(len(List[0])):
            if List[1] == "Even" and i % 2 == 1:
                l.append(List[0][i])
            elif List[1] == "Odd" and i % 2 == 0:
                l.append(List[0][i])
        return l


print("*** Odd Even ***")
input = input("Enter Input : ").split(",", 1)
print(odd_even(input[0], input[1]))
