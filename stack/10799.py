import sys
from collections import deque

stack = deque()


def push(x):
    global stack
    stack.append(x)


def pop():
    global stack
    if len(stack) > 0:
        print(stack.pop())
    else:
        print(-1)


def size():
    global stack
    print(len(stack))


def empty():
    global stack
    if len(stack) > 0:
        print(0)
    else:
        print(1)


def top():
    global stack
    if len(stack) > 0:
        print(stack[-1])
    else:
        print(-1)


# data = sys.stdin.readline().split()
data = input().split()
print(data)

for i in range(len(data[0])):
    print("data_count=", len(data[0]))
    push(data[0][i])

print(stack)
for i in range(len(stack)):
    pop()

