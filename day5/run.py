import re

seeds_matcher = re.compile("(seeds:)(.+)")
text_matcher = re.compile("\w+:")
number_matcher = re.compile("\d[\d\s]+")

with open('day5/files/data.txt') as f:

    lines = f.readlines()
    
    all_ranges = []
    for line in lines:
        seeds_line = seeds_matcher.findall(line)
        if seeds_line:
            seeds = [int(n) for n in seeds_line[0][1].strip().split(" ")]
        if 'map' in line:
            all_ranges.append([])
        if number_matcher.match(line):
            numbers = [int(n) for n in line.strip().split(" ") if not n == " "]
            dest, source, n = numbers
            r = all_ranges[-1]
            r.append(((source, source + n), dest - source))
    
    seed_ranges = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
    
    min_location = 1e10
    for seed_range in seed_ranges:
        print (seed_range)
        for n in range(seed_range[0], seed_range[0] + seed_range[1]):
            #print (n)
            result = n
            for ranges in all_ranges:
                for r in ranges:
                    (r1, r2), offset = r
                    if r1 <= result < r2:
                        result = result + offset
                        break 
            if result < min_location:
                min_location = result
    #print (locations)            
    print (min_location)
