from collections import deque

def bfs(node, tree, visited, wire):
    cnt = 0
    q = deque([node])
    visited[node] = True

    while q:
        node = q.popleft()
        cnt += 1

        for num in tree[node]:
            if not ((node == wire[0] and num == wire[1]) or (node == wire[1] and num == wire[0])):
                if not visited[num]:
                    visited[num] = True
                    q.append(num)

    return cnt


def solution(n, wires):
    answer = float('inf')
    tree = [[] for _ in range(n + 1)]

    for wire in wires:
        v1, v2 = wire
        tree[wire[0]].append(wire[1])
        tree[wire[1]].append(wire[0])

    for wire in wires:
        visited = [False] * (n + 1)
        tmp = []
        for i in range(1, n + 1):
            if not visited[i]:
                cnt = bfs(i, tree, visited, wire)
                tmp.append(cnt)
        answer = min(answer, abs(tmp[0] - tmp[1]))

    return answer