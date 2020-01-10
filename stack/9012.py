import sys
from collections import deque

stack = deque()


def push(x):
    global stack
    stack.append(x)


def pop():
    global stack
    if len(stack) > 0:
        stack.pop()


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


iteration = int(sys.stdin.readline())
total = 0

for i in range(iteration):
    # string = sys.stdin.readline()
    string = input()
    total = 0
    for j in range(len(stack)):
        pop()

    for j in range(len(string)):
        if string[j] == '(':
            push('(')
            total += 1
        else:
            pop()
            total -= 1

    if total == 0 and len(stack) == 0:
        print("YES")
    else:
        print("NO")
    # print("total: ", total)
    # print("stack_size: ", len(stack))
