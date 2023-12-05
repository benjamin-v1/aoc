from aocd import get_data
data = get_data(year=2023, day=5)

### PART A

example_data_a = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

example_answer_a = 35

def part_a(data):
    answer = 0

    return answer

print(part_a(example_data_a))

assert part_a(example_data_a) == example_answer_a, "Example for part a is wrong!"
print("Part a is: " + str(part_a(data)))


### PART B

# example_data_b = """
# """

# example_answer_b = 0


# def part_b(data):
#     answer = 0

#     return answer

# assert part_b(example_data_b) == example_answer_b, "Example for part b is wrong!"
# print("Part b is: " + str(part_b(data)))
