# CR. P'Pop sirawit
power, askList = input('Enter Input : ').split('/')

power = [int(x) for x in power.split()]
askList = [str(i) for i in askList.split(',')]


def powOf(n):
    sum = 0

    if n >= len(power):
        return 0

    sum += powOf(2 * n + 1)
    sum += powOf(2 * n + 2)
    return power[n] + sum


print(powOf(0))
for data in askList:
    powX = powOf(int(data[0]))
    powY = powOf(int(data[2]))
    if powX > powY:
        print(f"{data[0]}>{data[2]}")
    elif powX < powY:
        print(f"{data[0]}<{data[2]}")
    elif powX == powY:
        print(f"{data[0]}={data[2]}")
