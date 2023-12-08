import re
from typing import List, Set, Dict, Tuple


def getGears(numbersAround: List[List[Tuple[Tuple[int, int], int]]], gear: Tuple[int, int]):
    gears = []
    minChar, maxChar = gear
    for numbers in numbersAround:
        for number in numbers:    
            (minNum, maxNum), g = number      
            if maxChar >= minNum and minChar <= maxNum:
                gears.append(g)        

    if len(gears) == 2:
        return gears[0] * gears[1]
    return 0

numberMatcher = re.compile("\d+")
gearMatcher = re.compile("\*")

with open('day3/files/data.txt') as f:
    allNumbers = []
    allGears = []
    lines = f.readlines()
    for line in lines:
        allNumbers.append([(m.span(), int(m.group())) for m in numberMatcher.finditer(line.strip())])
        allGears.append([(m.span()) for m in gearMatcher.finditer(line.strip())])

    allOKGearRatios = []

    for i, gears in enumerate(allGears):
        if i > 0 and i < len(allNumbers) -1:
          allOKGearRatios.extend([getGears(allNumbers[i-1:i+2], gear) for gear in gears])

        


    print (allOKGearRatios)
    print (sum(allOKGearRatios))

