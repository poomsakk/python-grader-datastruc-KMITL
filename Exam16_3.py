count = 0


def bubble_sort(lst):
    global count
    n = len(lst)
    for i in range(n-1):
        continue_swap = True
        for j in range(n-i-1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                continue_swap = False
            count += 1
        if continue_swap:
            break


print(" *** Bubble sort ***")
input_string = input("Enter some numbers : ")
A = []
for n in input_string.split():
    A.append(int(n))
bubble_sort(A)
print()
print(A)
print("Data comparison =", count)
