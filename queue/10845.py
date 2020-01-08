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


push(1)
push(2)
front()
back()
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
front()
