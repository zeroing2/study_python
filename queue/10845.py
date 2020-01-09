from collections import deque

queue = deque()


def push(x):
    global queue
    queue.append(x)


def pop():
    global queue
    if len(queue) > 0:
        print(queue.popleft())
    else:
        print(-1)


def size():
    global queue
    print(len(queue))


def empty():
    global queue
    if len(queue) > 0:
        print(0)
    else:
        print(1)


def front():
    global queue
    if len(queue) > 0:
        print(queue[0])
    else:
        print(-1)


def back():
    global queue
    if len(queue) > 0:
        print(queue[-1])
    else:
        print(-1)


def execute_command(command):
    if 'push' in command:
        push(int(command[1]))
    elif 'pop' in command:
        pop()
    elif 'front' in command:
        front()
    elif 'back' in command:
        back()
    elif 'empty' in command:
        empty()
    elif 'size' in command:
        size()
    else:
        print("invalid command")


iteration_num = int(input())
for i in range(iteration_num):
    command = input().split()
    execute_command(command)