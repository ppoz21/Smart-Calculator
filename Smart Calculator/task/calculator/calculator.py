def operator_reader(operator):
    """ Simplifies extended operators, not much usefull now"""
    minuses = operator.count('-')
    if minuses % 2 == 0:
        return '+'
    else:
        return '-'


while True:
    text = input()
    if text == '/exit': break
    if text == '/help': print("The program calculates the sum of numbers, and is capable of processing double negatives")
    if text == '': continue
    tokens = text.split()
    total = int(tokens[0])
    operations = zip(tokens[1::2], tokens[2::2])  # Expected structure
    for operator, value in operations:
        operator = operator_reader(operator)
        total += int(operator + str(value))
    print(total)
print('Bye!')
