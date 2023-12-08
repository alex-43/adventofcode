from functools import reduce


with open('day6/files/data.txt') as f:

    lines = f.readlines()
    #times = [int (n) for n in lines[0].split(":")[1].strip().split(" ") if not n == ""]
    #dists = [int (n) for n in lines[1].split(":")[1].strip().split(" ") if not n == ""]

    times = [int (lines[0].split(":")[1].strip().replace(" ", ""))]
    dists = [int (lines[1].split(":")[1].strip().replace(" ", ""))]

    all_num_wins = []
    for max_time, max_dist in (zip(times, dists)):
        num_wins = 0
        for t in range(max_time):
            distance = t * (max_time - t)
            if distance > max_dist:
                num_wins += 1
        all_num_wins.append(num_wins)
    print (reduce(lambda a, b: a * b, all_num_wins))
    