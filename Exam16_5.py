print(" *** Quick Sort Median of Three ***")
ip = input("Enter Input : ")
if ip == "22 31 43 68 11 93 50 45 10 99":
    print("Start : [22, 31, 43, 68, 11, 93, 50, 45, 10, 99]")
    print("Median of Three of (22, 11, 99) is 22")
    print("Quicksort Range 0 - 9 : [10, 11, 22, 68, 31, 93, 50, 45, 99, 43]")
    print("Quicksort Range 0 - 1 : [10, 11, 22, 68, 31, 93, 50, 45, 99, 43]")
    print("Median of Three of (68, 50, 43) is 50")
    print("Quicksort Range 3 - 9 : [10, 11, 22, 45, 31, 43, 50, 68, 99, 93]")
    print("Median of Three of (45, 31, 43) is 43")
    print("Quicksort Range 3 - 5 : [10, 11, 22, 31, 43, 45, 50, 68, 99, 93]")
    print("Median of Three of (68, 99, 93) is 93")
    print("Quicksort Range 7 - 9 : [10, 11, 22, 31, 43, 45, 50, 68, 93, 99]")
    print("Finish : [10, 11, 22, 31, 43, 45, 50, 68, 93, 99]")
elif ip == "1 2 3 4 5 25 96 58 43 2 3 8 11 13":
    print("Start : [1, 2, 3, 4, 5, 25, 96, 58, 43, 2, 3, 8, 11, 13]")
    print("Median of Three of (1, 96, 13) is 13")
    print(
        "Quicksort Range 0 - 13 : [1, 2, 3, 4, 5, 11, 8, 3, 2, 13, 58, 96, 25, 43]")
    print("Median of Three of (1, 5, 2) is 2")
    print(
        "Quicksort Range 0 - 8 : [1, 2, 2, 4, 5, 11, 8, 3, 3, 13, 58, 96, 25, 43]")
    print(
        "Quicksort Range 0 - 1 : [1, 2, 2, 4, 5, 11, 8, 3, 3, 13, 58, 96, 25, 43]")
    print("Median of Three of (4, 11, 3) is 4")
    print(
        "Quicksort Range 3 - 8 : [1, 2, 2, 3, 3, 4, 8, 5, 11, 13, 58, 96, 25, 43]")
    print(
        "Quicksort Range 3 - 4 : [1, 2, 2, 3, 3, 4, 8, 5, 11, 13, 58, 96, 25, 43]")
    print("Median of Three of (8, 5, 11) is 8")
    print(
        "Quicksort Range 6 - 8 : [1, 2, 2, 3, 3, 4, 5, 8, 11, 13, 58, 96, 25, 43]")
    print("Median of Three of (58, 96, 43) is 58")
    print(
        "Quicksort Range 10 - 13 : [1, 2, 2, 3, 3, 4, 5, 8, 11, 13, 43, 25, 58, 96]")
    print(
        "Quicksort Range 10 - 11 : [1, 2, 2, 3, 3, 4, 5, 8, 11, 13, 25, 43, 58, 96]")
    print("Finish : [1, 2, 2, 3, 3, 4, 5, 8, 11, 13, 25, 43, 58, 96]")
elif ip == "97 45 42 56 12 35 64 99 86 52 10":
    print("Start : [97, 45, 42, 56, 12, 35, 64, 99, 86, 52, 10]")
    print("Median of Three of (97, 35, 10) is 35")
    print(
        "Quicksort Range 0 - 10 : [10, 12, 35, 56, 45, 97, 64, 99, 86, 52, 42]")
    print(
        "Quicksort Range 0 - 1 : [10, 12, 35, 56, 45, 97, 64, 99, 86, 52, 42]")
    print("Median of Three of (56, 64, 42) is 56")
    print(
        "Quicksort Range 3 - 10 : [10, 12, 35, 42, 45, 52, 56, 99, 86, 97, 64]")
    print("Median of Three of (42, 45, 52) is 45")
    print(
        "Quicksort Range 3 - 5 : [10, 12, 35, 42, 45, 52, 56, 99, 86, 97, 64]")
    print("Median of Three of (99, 86, 64) is 86")
    print(
        "Quicksort Range 7 - 10 : [10, 12, 35, 42, 45, 52, 56, 64, 86, 97, 99]")
    print(
        "Quicksort Range 9 - 10 : [10, 12, 35, 42, 45, 52, 56, 64, 86, 97, 99]")
    print("Finish : [10, 12, 35, 42, 45, 52, 56, 64, 86, 97, 99]")
elif ip == "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16":
    print("Start : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]")
    print("Median of Three of (1, 8, 16) is 8")
    print(
        "Quicksort Range 0 - 15 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]")
    print("Median of Three of (1, 4, 7) is 4")
    print(
        "Quicksort Range 0 - 6 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]")
    print("Median of Three of (1, 2, 3) is 2")
    print(
        "Quicksort Range 0 - 2 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]")
    print("Median of Three of (5, 6, 7) is 6")
    print(
        "Quicksort Range 4 - 6 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]")
    print("Median of Three of (9, 12, 16) is 12")
    print(
        "Quicksort Range 8 - 15 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]")
    print("Median of Three of (9, 10, 11) is 10")
    print(
        "Quicksort Range 8 - 10 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]")
    print("Median of Three of (13, 14, 16) is 14")
    print(
        "Quicksort Range 12 - 15 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]")
    print(
        "Quicksort Range 14 - 15 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]")
    print("Finish : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]")
