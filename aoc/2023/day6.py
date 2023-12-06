from aocd import get_data
data = get_data(year=2023, day=6)

### PART A

example_data_a = """Time:      7  15   30
Distance:  9  40  200"""

example_answer_a = 288

def part_a(data):
    import re

    answer = 0
    races = []

    tmp = re.findall(r'(\d+)',data)
    times = tmp[:int(len(tmp)/2)]
    distances = tmp[int(len(tmp)/2):]

    i = 0
    while i < int((len(tmp)/2)):
        races.append({'time':times[i], 'distance':distances[i]})
        i += 1


    for race in races:
        i = 1
        winning_times = 0
        time = int(race['time'])
        record_distance = int(race['distance'])
        while i < time:
            remaining_time = time - i
            distance = remaining_time * i
            if distance > record_distance:
                winning_times += 1
            i += 1
        if answer == 0:
            answer = winning_times
        else:
            answer = answer * winning_times

    return answer


# assert part_a(example_data_a) == example_answer_a, "Example for part a is wrong!"
# print("Part a is: " + str(part_a(data)))


### PART B

example_data_b = """Time:      7  15   30
Distance:  9  40  200"""

example_answer_b = 71503


def part_b(data):
    import re

    answer = 0
    races = []

    tmp = re.findall(r'(\d+)',data)
    time = int(''.join(re.findall(r'(\d+)' ,data.split('\n')[0])))
    record_distance = int(''.join(re.findall(r'(\d+)' ,data.split('\n')[1])))

    winning_times = 0
    i = 1
    # lets brute force this as i am too stupid to know how else to do it
    while i < time:
        remaining_time = time - i
        distance = remaining_time * i
        if distance > record_distance:
            winning_times += 1
        i += 1

    return winning_times

assert part_b(example_data_b) == example_answer_b, "Example for part b is wrong!"
print("Part b is: " + str(part_b(data)))
