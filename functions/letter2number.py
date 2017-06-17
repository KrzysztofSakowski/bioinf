def letter2number(character):
    numbers = {
        '-' : 1,
        'A' : 2,
        'C' : 3,
        'D' : 4,
        'E' : 5,
        'F' : 6,
        'G' : 7,
        'H' : 8,
        'I' : 9,
        'K' : 10,
        'L' : 11,
        'M' : 12,
        'N' : 13,
        'P' : 14,
        'Q' : 15,
        'R' : 16,
        'S' : 17,
        'T' : 18,
        'V' : 19,
        'W' : 20,
        'Y' : 21
    }

    if character in numbers.keys():
        return numbers[character]
    else:
        return 1
