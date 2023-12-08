

with open('day8/files/data.txt') as f:
    lines = f.readlines()
    instruction_line = lines[0]
    instructions = [0 if c == "L" else 1 for c in instruction_line.strip()]

    node_map = {}
    for line in lines[2:]:
        node, pair = line.split("=")
        pair = pair.replace("(", "")
        pair = pair.replace(")", "")
        lr = pair.split(",")
        node_map[node.strip()] = [lr[0].strip(), lr[1].strip()]
    #print (node_map)

    steps = 0
    instruction_index = 0
    node = "AAA"
    while node != "ZZZ":
        instruction = instructions[instruction_index]
        node = node_map[node][instruction]
        instruction_index += 1
        if instruction_index == len(instructions):
            instruction_index = 0
        steps += 1
    print (steps)
