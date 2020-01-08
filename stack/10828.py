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


push(1)
push(2)
top()
size()
empty()
pop()
pop()
pop()
size()
empty()
pop()
push(3)
empty()
top()