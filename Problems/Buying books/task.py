n = int(input())
books = []
for _i in range(n):
    action = input().split(" ", 1)
    if action[0] == "BUY":
        books.append(action[1])
    elif action[0] == "READ":
        print(books.pop())
