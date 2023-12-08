from aocd import get_data
data = get_data(year=2023, day=8)

### PART A

example_data_a = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

example_answer_a = 6

def part_a(data):
    import re

    answer = 0
    nodes = {}

    directions = data.split('\n')[0]
    datas = re.findall(r"(.{3}) \= \((.{3})\, (.{3})\)",data)
    for data in datas:
        nodes[data[0]] = {"L": data[1], "R": data[2]}

    current_node = "AAA"
    desired_node = "ZZZ"

    i = 0
    test = True
    while test == True:
        if i == len(directions):
            i = 0
        direction = directions[i]
        current_node = nodes[current_node][direction]
        i += 1
        answer += 1 
        if current_node == desired_node:
            test = False
    
    
    return answer

# print(part_a(example_data_a))
# assert part_a(example_data_a) == example_answer_a, "Example for part a is wrong!"
print("Part a is: " + str(part_a(data)))


### PART B

# example_data_b = """
# """

# example_answer_b = 0


# def part_b(data):
#     answer = 0

#     return answer

# print(part_b(example_data_b))
# assert part_b(example_data_b) == example_answer_b, "Example for part b is wrong!"
# print("Part b is: " + str(part_b(data)))
