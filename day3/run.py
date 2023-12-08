import re
from typing import List, Set, Dict, Tuple

def ok(number: Tuple[Tuple[int, int], int], charactersList: List[List[Tuple[int, int]]]):
    ((minNum, maxNum), _) = number
    for characters in charactersList:
        for minChar, maxChar in characters:
            if maxChar >= minNum and minChar <= maxNum:
                return True

    return False

def getGears(numbers: List[Tuple[Tuple[int, int], int]], gears: List[Tuple[int, int]]):

    ((minNum, maxNum), _) = number
    for minChar, maxChar in gears:
        

        if maxChar >= minNum and minChar <= maxNum:
            return True
    return []

numberMatcher = re.compile("\d+")
specialCharMatcher = re.compile("[^\d.]")
gearMatcher = re.compile("\*")

with open('day3/files/data.txt') as f:
    allNumbers = []
    allCharacters = []
    lines = f.readlines()
    for line in lines:

        allNumbers.append([(m.span(), int(m.group())) for m in numberMatcher.finditer(line.strip())])
        allCharacters.append([(m.span()) for m in specialCharMatcher.finditer(line.strip())])
    allOKNumbers = []
    for i, numbers in enumerate(allNumbers):
        charLines = [allCharacters[i]]
        if i > 0:
            charLines.append(allCharacters[i - 1])
        if i < len(allNumbers) -1 :
            charLines.append(allCharacters[i + 1])
        
        allOKNumbers.extend([number[1] for number in numbers if ok(number, charLines)])



    print (sum(allOKNumbers))

