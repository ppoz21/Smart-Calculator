guests = []

while True:
    guest = input()
    if guest == '.':
        break
    else:
        guests.append(guest)

print(guests)
print(len(guests))
