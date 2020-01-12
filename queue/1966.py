class Node:
    def __init__(self, priority, first_index):
        self.priority = priority
        self.first_index = first_index

    def get_priority(self):
        return self.priority

    def get_first_index(self):
        return self.first_index


q = list()

iteration_num = int(input())
for i in range(iteration_num):
    cmd = list(map(int, input().split()))
    priority = list(map(int, input().split()))
    target_index = cmd[1]
    # print(cmd)
    # print(priority)
    for j in range(len(priority)):
        node = Node(priority[j], j)
        q.append(node)

    cnt = 0
    while len(q) > 0:
        greater = False
        equal = False
        pop_priority = q[0].get_priority()
        pop_index = q[0].get_first_index()
        del q[0]

        for j in range(len(q)):
            if pop_priority < q[j].get_priority():
                greater = True
            elif pop_priority == q[j].get_priority():
                equal = True

        if target_index == pop_index:
            if greater:
                node = Node(pop_priority, pop_index)
                q.append(node)
            else:
                cnt = cnt + 1
                break
        else:
            if greater:
                node = Node(pop_priority, pop_index)
                q.append(node)
            else:
                cnt = cnt + 1

    print(cnt)
    q.clear()
