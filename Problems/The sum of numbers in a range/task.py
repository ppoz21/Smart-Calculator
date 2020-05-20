def range_sum(numbers, a, b):
    a = int(a)
    b = int(b)
    num_of_els = 0
    for number in numbers:
        if a <= int(number) <= b:
            num_of_els += int(number)
    return num_of_els


numbers = input().split(" ")
a, b = input().split(" ")
print(range_sum(numbers, a, b))
