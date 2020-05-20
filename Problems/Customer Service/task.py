from collections import deque

n = int(input())
queue = deque()

for i in range(n):
    task = input().split(" ")
    if len(task) == 1 and task[0] == "SOLVED":
        queue.popleft()
    elif len(task) == 2:
        queue.append(int(task[1]))

for el in queue:
    print(el)
