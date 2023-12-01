def my_w2n(number_string):
    digits = {
        "zero"  : 0,
        "one"   : 1,
        "two"   : 2,
        "three" : 3,
        "four"  : 4,
        "five"  : 5,
        "six"   : 6,
        "seven" : 7,
        "eight" : 8,
        "nine"  : 9
    }

    if number_string in digits:
        return digits[number_string]
    return number_string

print(my_w2n("2"))