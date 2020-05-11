card_values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14
}

c1 = input()
c2 = input()
c3 = input()
c4 = input()
c5 = input()
c6 = input()

suma = (card_values[c1] + card_values[c2] + card_values[c3] + card_values[c4] + card_values[c5] + card_values[c6])

print(suma / 6)
