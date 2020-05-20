from collections import deque
n = int(input())
students = deque()
passed = deque()

for i in range(n):
    task = input()
    if task == "PASSED":
        passed.append(students.pop())
    elif task == "EXTRA":
        students.appendleft(students.pop())
    else:
        students.appendleft(task.split(" ")[1])

for student in passed:
    print(student)
