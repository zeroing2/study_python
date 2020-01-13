import sys

iteration = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort(reverse=True)
b.sort()

result = 0
for i in range(iteration):
    result += a[i] * b[i]

print(result)