
def get_score(win_numbers, numbers):
    faculty = 0

    for n in numbers:
        if n in win_numbers:
            if faculty == 0:
                faculty = 1
            else:
                faculty *= 2
    return faculty

def get_winning_numbers_count(win_numbers, numbers):
    result = 0

    for n in numbers:
        if n in win_numbers:
                result += 1
    return result

with open('day4/files/data.txt') as f:

    lines = f.readlines()
    wins = []
    scores = []
    win_numbers_counts = []

    for index, line in enumerate(lines):
        data = line.split(":")
        win, nums = data[1].split("|")

        win_numbers = [int(n) for n in win.strip().split(" ") if not n == ""]
        numbers = [int(n) for n in nums.strip().split(" ") if not n == ""]

        faculty = get_score(win_numbers, numbers)
        win_numbers_count = get_winning_numbers_count(win_numbers, numbers)
        wins.append(faculty)
        win_numbers_counts.append((index, win_numbers_count))
    print (sum(wins))

    new_win_numbers_counts = [s for s in win_numbers_counts]
    i = 0
    while True:
        index, s = new_win_numbers_counts[i]
        for j in range(s):
            if index + j + 1 < len(win_numbers_counts):
                new_win_numbers_counts.append(win_numbers_counts[index + j + 1])
        i += 1
        if i >= len(new_win_numbers_counts):
            break
    print (len(new_win_numbers_counts))