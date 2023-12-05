from aocd import get_data
data = get_data(year=2023, day=4)

### PART A

example_data_a = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

example_answer_a = 13

def part_a(data):
    import re

    answer = 0

    for card in data.split('\n'):
        card_score = 0
        tmp = re.findall(r'Card.*(\d{1,}): (.*)\|(.*)$', card)
        # card_id = int(tmp[0][0])
        winning_numbers = list(map(int, filter(None, tmp[0][1].strip().split(' '))))
        have_numbers = list(map(int, filter(None, tmp[0][2].strip().split(' '))))

        for winning_number in winning_numbers:
            if winning_number in have_numbers:
                if card_score == 0:
                    card_score = 1
                else:
                    card_score = card_score * 2
        answer += card_score  

    return answer

# print(part_a(example_data_a))
# assert part_a(example_data_a) == example_answer_a, "Example for part a is wrong!"
# print("Part a is: " + str(part_a(data)))


### PART B

example_data_b = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

example_answer_b = 30

CARD_DATA = {}
CARDS = []

def process_card(card_id):
    global CARDS
    global CARD_DATA
    cards_won = CARD_DATA[card_id]
    for card_won in cards_won:
        CARDS.append(card_won)
        process_card(card_won)

def part_b(data):
    import re

    global CARDS
    global CARD_DATA
    
    for card in data.split('\n'):
        tmp = re.findall(r'Card\ *(\d{1,}): (.*)\|(.*)$', card)
        card_id = int(tmp[0][0])
        winning_numbers = list(map(int, filter(None, tmp[0][1].strip().split(' '))))
        have_numbers = list(map(int, filter(None, tmp[0][2].strip().split(' '))))

        winning_cards = []
        winning_card_count = 0

        for winning_number in winning_numbers:
            if winning_number in have_numbers:
                winning_card_count += 1
                winning_cards.append(card_id + winning_card_count)

        CARD_DATA[card_id] = winning_cards

    for card_to_process in CARD_DATA:
        CARDS.append(card_to_process)
        process_card(card_to_process)
    
    return len(CARDS)

# print(part_b(example_data_b))
assert part_b(example_data_b) == example_answer_b, "Example for part b is wrong!"
print("Part b is: " + str(part_b(data)))
