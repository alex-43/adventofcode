from typing import List, Dict, Tuple
from functools import reduce

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def ok(dictList: List[Dict[str, int]]):
    for d in dictList: 
        if "blue" in d and d["blue"] > MAX_BLUE:
            return False
        if "red" in d and d["red"] > MAX_RED:
            return False
        if "green" in d and d["green"] > MAX_GREEN:
             return False
    return True

def maxNumbers(dictList: List[Dict[str, int]]):

    all = {}

    for d in dictList: 

        for key in ["blue", "red", "green"]:
            if key in d:
                if not key in all or d[key] > all[key]:
                    all[key] = d[key]

    return reduce(lambda a, b : a * b, all.values())


with open('day2/files/data.txt') as f:

    lines = f.readlines()
    ids = []
    maxNums = []
    for line in lines:
        game, data = line.strip().split(":")
        _, id = game.split(" ")
        draws = data.split(";")
        cubeData = [{c.strip().split(" ")[1] : int(c.strip().split(" ")[0]) for c in d.split(',')}  for  d in draws ]
        
        colors = {}

        if ok(cubeData): 
            ids.append(int(id))
        maxNums.append(maxNumbers(cubeData))

    print (sum(ids))
    print (sum(maxNums))
