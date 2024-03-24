S = lambda: map(int, input().split())
L = lambda: list(S())


def dfs(ng, gph, start):
    history = []
    visited = [-1] * ng
    fromwhere = [0] * ng
    to_visit = [start]
    dph = 0
    while(len(to_visit) > 0):
        node = to_visit.pop()
        if visited[node] == -1:
            visited[node] = visited[fromwhere[node]] + 1
            to_visit.extend(gph[node])
            for x in gph[node]:
                if visited[x] == -1:
                    fromwhere[x] = node
    max_dph = -1
    ans = -1
    print(visited)
    for i in range(ng):
        if visited[i] > max_dph:
            ans = i
            max_dph = visited[i]
    return ans


def solve():
    n = int(input())
    gph = [[] for _ in range(n)]
    for vert in range(n-1):
        u, v = S()
        gph[u-1].append(v-1)
        gph[v-1].append(u-1)
    print(gph)
    f1 = dfs(n, gph, 0)
    f2 = dfs(n, gph, f1)
    print(f1, f2)

    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()

