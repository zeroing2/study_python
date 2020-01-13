import sys

n_k = list(map(int, sys.stdin.readline().split()))

data = list()
for i in range(n_k[0]):
    data.append(int(sys.stdin.readline()))

data.sort(reverse=True)

print("data: ", data)

coin_cnt = 0
for i in range(len(data)):
    k = 0
    while (data[i] * k) <= n_k[1]:
        k = k + 1
        if(data[i] * k) > n_k[1]:
            n_k[1] -= (data[i] * k-1)
            break

    coin_cnt += k
