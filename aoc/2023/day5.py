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

def make_array(lines, name):
    print('Creating ',name)
    array = []
    for line in lines:
        if line:
            line_dict = {}
            d = line.split(' ')
            line_dict['source_start'] = int(d[1])
            line_dict['source_end'] = int(d[1])+int(d[2])
            line_dict['destination'] = int(d[0])
            array.append(line_dict)
    return array

def check_array(array,value):
    destination = 0
    for rule in array:
        if rule['source_start'] <= value <= rule['source_end']:
            destination = rule['destination'] + (value - rule['source_start'])
            return destination 
    if destination == 0:
        return value


def part_a(data):
    import re
    answer = 0
    locations = []
    print('getting data...')
    tmp = re.findall(r'seeds: (.*)\n\nseed-to-soil map:\n((.|\n)*)\nsoil-to-fertilizer map:\n((.|\n)*)\nfertilizer-to-water map:\n((.|\n)*)\nwater-to-light map:\n((.|\n)*)\nlight-to-temperature map:\n((.|\n)*)\ntemperature-to-humidity map:\n((.|\n)*)\nhumidity-to-location map:\n((.|\n)*)',data)

    seeds = list(map(int,tmp[0][0].split(' ')))
    print('Creating arrays')
    ss_array = make_array(tmp[0][1].split('\n'),'ss_array')
    sf_array = make_array(tmp[0][3].split('\n'),'sf_array')
    fw_array = make_array(tmp[0][5].split('\n'),'fw_array')
    wl_array = make_array(tmp[0][7].split('\n'),'wl_array')
    lt_array = make_array(tmp[0][9].split('\n'),'lt_array')
    th_array = make_array(tmp[0][11].split('\n'),'th_array')
    hl_array = make_array(tmp[0][13].split('\n'),'hl_array')

    for seed in seeds:
        # This is going to be horrid....
        so = check_array(ss_array,seed)
        fu = check_array(sf_array,so)
        wa = check_array(fw_array,fu)
        li = check_array(wl_array,wa)
        te = check_array(lt_array,li)
        hu = check_array(th_array,te)
        lo = check_array(hl_array,hu)

        locations.append(lo)

        print('SEED', seed)
        print('so: ',so)
        print('fu: ',fu)
        print('wa: ',wa)
        print('li: ',li)
        print('te: ',te)
        print('hu: ',hu)
        print('lo: ',lo)
        print('\n')

    answer = min(locations)
    return answer

# print(part_a(example_data_a))
assert part_a(example_data_a) == example_answer_a, "Example for part a is wrong!"
# print("Part a is: " + str(part_a(data)))


### PART B

example_data_b = example_data_a

example_answer_b = 46

def part_b(data):
    import re
    answer = 0
    locations = []
    seed_ranges = []
    print('getting data...')
    tmp = re.findall(r'seeds: (.*)\n\nseed-to-soil map:\n((.|\n)*)\nsoil-to-fertilizer map:\n((.|\n)*)\nfertilizer-to-water map:\n((.|\n)*)\nwater-to-light map:\n((.|\n)*)\nlight-to-temperature map:\n((.|\n)*)\ntemperature-to-humidity map:\n((.|\n)*)\nhumidity-to-location map:\n((.|\n)*)',data)

    seed_res = re.findall(r'((\d*) (\d*)) ?',tmp[0][0])
    for seed_re  in seed_res:
        seed_ranges.append({'start':int(seed_re[1]),'end':int(seed_re[1]) + int(seed_re[2])-1})

    print('Creating arrays')
    ss_array = make_array(tmp[0][1].split('\n'),'ss_array')
    sf_array = make_array(tmp[0][3].split('\n'),'sf_array')
    fw_array = make_array(tmp[0][5].split('\n'),'fw_array')
    wl_array = make_array(tmp[0][7].split('\n'),'wl_array')
    lt_array = make_array(tmp[0][9].split('\n'),'lt_array')
    th_array = make_array(tmp[0][11].split('\n'),'th_array')
    hl_array = make_array(tmp[0][13].split('\n'),'hl_array')

    for seed_range in seed_ranges:
        seed = seed_range['start']
        print('Range: ', seed , ' to ', seed_range['end'])

        while seed <= seed_range['end']:
            # This is going to be horrid....
            so = check_array(ss_array,seed)
            fu = check_array(sf_array,so)
            wa = check_array(fw_array,fu)
            li = check_array(wl_array,wa)
            te = check_array(lt_array,li)
            hu = check_array(th_array,te)
            lo = check_array(hl_array,hu)

            locations.append(lo)

            # print('SEED', seed)
            # print('so: ',so)
            # print('fu: ',fu)
            # print('wa: ',wa)
            # print('li: ',li)
            # print('te: ',te)
            # print('hu: ',hu)
            # print('lo: ',lo)
            # print('\n')

            seed += 1

    answer = min(locations)
    return answer

# assert part_b(example_data_b) == example_answer_b, "Example for part b is wrong!"
print("Part b is: " + str(part_b(data)))
