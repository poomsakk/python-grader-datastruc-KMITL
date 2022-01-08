# CR. P'Pop sirawit
k, dayList = input('Enter Input : ').split('/')
dayList = [int(i) for i in dayList.split()]

num = []
van = {}    # dict

for i in range(int(k)):
    num.append(i + 1)           # number of van
    # set day to 0 of van  // .get(data, defaultNum)
    van[i+1] = van.get(i+1, 0)

for i in range(len(dayList)):
    minNum = num.pop(0)
    # add day reserve by dayList[i]
    van[minNum] = van.get(minNum, 0) + int(dayList[i])
    print(f'Customer {i+1} Booking Van {minNum} | {dayList[i]} day(s)')

    for index in range(len(num)):   # run every index

        # day[0] < day[1,2,3,4,5,6,7,8...] // day[0] == day[1,2,3,4,5,6,7,8...] and minNum < number (same day..different number)
        if van[minNum] < van[num[index]] or (van[minNum] == van[num[index]] and minNum < num[index]):
            num.insert(index, minNum)  # sorted and insert min between list
            minNum = None
            break

    if minNum is not None:  # if can't insert and have minNum
        num.append(minNum)  # append last one to num
