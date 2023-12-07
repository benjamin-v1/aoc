from aocd import get_data
data = get_data(year=2023, day=7)

### PART A

example_data_a = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

example_answer_a = 6440

def hand_values(hand):
    new_hand = []
    card_values = {
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14 
    }
    for card in hand:
        new_hand.append(int(card_values.get(card, card)))
    return new_hand

def score_hand(values):
    pairs = {}
    cards = []
    t = ""

    for x in values:
            if x not in pairs:
                cards.append(x)
            pairs[x] = pairs.get(x, 0) + 1
            t = t + str(x).zfill(2)

    if len(cards) == 1:
        s = 7
    
    elif len(cards) == 2:
        if pairs[cards[0]] == 4 or pairs[cards[1]] == 4:
            s = 6
        else: 
            s = 5

    elif len(cards) == 3:
        if pairs[cards[0]] == 3 or pairs[cards[1]] == 3 or pairs[cards[2]] == 3:
            s = 4
        else:
            s = 3

    elif len(cards) == 4:             
        s = 2
    
    elif len(cards) == 5:
        s = 1

    return int(str(s)+str(t))


def part_a(data):
    import re
    from operator import itemgetter
    
    rankings = []
    answer = 0
    for round in data.split('\n'):
        hand,bid = re.findall(r'^(.{5}) (\d*)$', round)[0]
        score = score_hand(hand_values(hand))
        rankings.append({
            "hand":hand,
            "score":score,
            "bid":bid
            })
        
    i = 1
    for rank in sorted(rankings, key=itemgetter('score')):
        answer += int(rank['bid']) * i
        i += 1

    return answer

# print(part_a(example_data_a))
assert part_a(example_data_a) == example_answer_a, "Example for part a is wrong!"
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
