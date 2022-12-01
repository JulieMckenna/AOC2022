
elfIndex = 0
elfCals = {0: 0}
with open('AOC01.txt', 'r') as f:
    lines = f.read().splitlines()
for cal in lines:
    if (cal == ""):
        elfIndex += 1
        elfCals[elfIndex] = 0
    else:
        elfCals[elfIndex] += int(cal)


def FindMax(elfCals):
    max = 0
    maxElfNum = 0
    for elf in elfCals:
        if (elfCals[elf] > max):
            max = elfCals[elf]
            maxElfNum = elf
    print("max cals: " + str(max) + ", elf num: " + str(maxElfNum))
    return [maxElfNum, max]


FindMax(elfCals)


def FindTopThree(elfCals):
    first = FindMax(elfCals)
    elfCals[first[0]] = 0
    second = FindMax(elfCals)
    elfCals[second[0]] = 0
    third = FindMax(elfCals)
    sum = first[1] + second[1] + third[1]
    print(sum)


FindTopThree(elfCals)
