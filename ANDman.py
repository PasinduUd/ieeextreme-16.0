# 33.34%

import math
from collections import defaultdict

t = int(input())


def get_path(_visited, x, y, path):
    global path_found, cache
    path.append(x)
    if x == y:
        cache[(path[0], y)] = path
        mul = 1
        for i in path:
            mul *= nodes[i - 1]
        print(mul % (int(math.pow(10, 9) + 7)))
        path_found = True
        return
    _visited[x] = True
    if (x, y) in cache:
        path += cache[(x, y)][1:]
        mul = 1
        for i in path:
            mul *= nodes[i - 1]
        print(mul % (int(math.pow(10, 9) + 7)))
        path_found = True
        return

    if len(edges[x]) > 0:
        for j in edges[x]:
            if not _visited[j]:
                get_path(_visited, j, y, path)

    del path[-1]


for _ in range(t):
    n = int(input())
    nodes = list(map(int, input().strip().split()))
    edges = [[] for j in range(n + 1)]
    for l in range(n - 1):
        a, b = map(int, input().strip().split())
        edges[a].append(b)
        edges[b].append(a)
    q = int(input())
    for i in range(q):
        t, u, v = map(int, input().strip().split())
        if t == 1:
            nodes[u - 1] = v
        elif t == 2:
            visited = [False for i in range(n + 1)]
            path_found = False
            cache = defaultdict(lambda: float('inf'))
            get_path(visited, u, v, [])
            if not path_found:
                print(0)
