from aocd import get_data
data = get_data(year=2023, day=1)

### PART A

example_data_a = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

example_answer_a = 142

def part_a(data):
    import re

    answer = 0

    for line in data.split("\n"):
        temp = re.findall(r'\d{1}+', line)
        numbers = list(map(int, temp))
        answer += int(str(numbers[0]) + str(numbers[-1]))

    return answer

assert part_a(example_data_a) == example_answer_a, "Example for part a is wrong!"
print("Part a is: " + str(part_a(data)))


### PART B

example_data_b = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

example_answer_b = 281


def part_b(data):

    import re
    from ..aoc import my_w2n

    answer = 0

    for line in data.split("\n"):
        tmp = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d{1}))', line)
        numbers = [my_w2n(chr) for chr in tmp]
        digit = int(str(numbers[0]) + str(numbers[-1]))
        answer += digit
    return answer


assert part_b(example_data_b) == example_answer_b, "Example for part b is wrong!"
print("Part b is: " + str(part_b(data)))
