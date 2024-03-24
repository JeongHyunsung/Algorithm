S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    a = L()
    m = int(input())
    mr, ml = [], []
    a_wi = []
    for idx, i in enumerate(a):
        a_wi.append([i, idx])
    a_wi.sort(key = lambda x: x[0], reverse = False)
    wh = [-1] * n
    for idx, i in enumerate(a_wi):
        wh[i[1]] = idx
        if idx == 0:
            mr.append(1)
            ml.append(0)
        elif idx == n-1:
            mr.append(0)
            ml.append(1)
        else:
            if (a_wi[idx][0] - a_wi[idx-1][0]) > (a_wi[idx+1][0] - a_wi[idx][0]):
                mr.append(1)
                ml.append(a_wi[idx][0] - a_wi[idx-1][0])
            else:
                mr.append(a_wi[idx+1][0] - a_wi[idx][0])
                ml.append(1)
    sm = 0
    for i in range(n):
        sm += mr[i]
        mr[i] = sm
    sm = 0
    for i in range(n-1, -1, -1):
        sm += ml[i]
        ml[i] = sm

    for i in range(m):
        x, y = S()
        x, y = x-1, y-1
        x, y = wh[x], wh[y]
        if x < y:
            up = mr[y-1]
            if x == 0:
                dw = 0
            else:
                dw = mr[x-1]
        else:
            up = ml[y+1]
            if x == n-1:
                dw = 0
            else:
                dw = ml[x+1]
        print(up-dw)

    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
