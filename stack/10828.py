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


def execute_command(command):
    if 'push' in command:
        push(int(command[1]))
    elif 'pop' in command:
        pop()
    elif 'top' in command:
        top()
    elif 'empty' in command:
        empty()
    elif 'size' in command:
        size()
    else:
        print("invalid command")


iteration_num = int(input())
for i in range(iteration_num):
    command = sys.stdin.readline().split()
    execute_command(command)