from aocd import get_data
data = get_data(year=2023, day=2)

### PART A

example_data_a = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

example_answer_a = 8

def part_a(data):
    import re

    answer = 0
    for game in data.split('\n'):
        temp = re.findall(r'(Game (\d{1,})): (.*)',game)
        if temp:
            game = int(temp[0][1])
            rounds = temp[0][2]
            results = {
                'red': [],
                'green': [],
                'blue': []
            }
            for round in rounds.split(';'):
                # I am not happy about this....
                results['red'].append(int(re.findall(r'(\d{1,}) red',round)[0]) if 'red' in round else 0)
                results['blue'].append(int(re.findall(r'(\d{1,}) blue',round)[0]) if 'blue' in round else 0)
                results['green'].append(int(re.findall(r'(\d{1,}) green',round)[0]) if 'green' in round else 0)

            m_blue = max(results['blue'])
            m_green = max(results['green'])
            m_red = max(results['red'])

            if m_blue <= 14 and m_red <= 12 and m_green <= 13:
                answer += game

    return answer

assert part_a(example_data_a) == example_answer_a, "Example for part a is wrong!"
print("Part a is: " + str(part_a(data)))


### PART B

example_data_b = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# """

example_answer_b = 2286


def part_b(data):
    answer = 0

    return answer

# assert part_b(example_data_b) == example_answer_b, "Example for part b is wrong!"
# print("Part b is: " + str(part_b(data)))
