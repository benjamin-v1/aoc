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

def make_map(lines, name):
    print('Creating ', name)
    map = {}
    for line in lines:
        if line:
            i = 0
            d = line.split(' ')
            while i < int(d[2]):
                map[int(d[1])+i] = int(d[0])+i
                i += 1
    return dict(sorted(map.items()))

def part_a(data):
    import re
    answer = 0
    locations = []
    print('getting data...')
    tmp = re.findall(r'seeds: (.*)\n\nseed-to-soil map:\n((.|\n)*)\nsoil-to-fertilizer map:\n((.|\n)*)\nfertilizer-to-water map:\n((.|\n)*)\nwater-to-light map:\n((.|\n)*)\nlight-to-temperature map:\n((.|\n)*)\ntemperature-to-humidity map:\n((.|\n)*)\nhumidity-to-location map:\n((.|\n)*)',data)

    seeds = list(map(int,tmp[0][0].split(' ')))
    print('Creating maps')
    ss_map = make_map(tmp[0][1].split('\n'),'ss_map')
    sf_map = make_map(tmp[0][3].split('\n'),'sf_map')
    fw_map = make_map(tmp[0][5].split('\n'),'fw_map')
    wl_map = make_map(tmp[0][7].split('\n'),'wl_map')
    lt_map = make_map(tmp[0][9].split('\n'),'lt_map')
    th_map = make_map(tmp[0][11].split('\n'),'th_map')
    hl_map = make_map(tmp[0][13].split('\n'),'hl_map')

    for seed in seeds:
        # This is going to be horrid....
        so = ss_map.get(seed, seed)
        fu = sf_map.get(so,so)
        wa = fw_map.get(fu,fu)
        li = wl_map.get(wa,wa)
        te = lt_map.get(li,li)
        hu = th_map.get(te,te)
        lo = hl_map.get(hu,hu)

        locations.append(lo)

        print('SEED', seed)
        print('so: ',so)
        print('fu: ',fu)
        print('wa: ',wa)
        print('li: ',li)
        print('te: ',te)
        print('hu: ',hu)
        print('lo: ',lo)

    answer = min(locations)
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

# assert part_b(example_data_b) == example_answer_b, "Example for part b is wrong!"
# print("Part b is: " + str(part_b(data)))
