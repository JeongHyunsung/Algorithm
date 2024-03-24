S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n, k = S()
    l = L()
    counter = {}
    setl = set()
    setr = set()
    seto = set()
    for i in l[:n]:
        if i in counter.keys():
            counter[i] += 1
        else:
            counter[i] = 1
    for key in counter.keys():
        if counter[key] == 2:
            setl.add(key)
        else:
            seto.add(key)
    for i in range(1, n+1):
        if i not in setl and i not in seto:
            setr.add(i)
    ans1, ans2 = [], []
    for i in range(k):
        if len(setl) > 0:
            x = setl.pop()
            y = setr.pop()
            ans1.append(x)
            ans1.append(x)
            ans2.append(y)
            ans2.append(y)
        else:
            x = seto.pop()
            y = seto.pop()
            ans1.append(x)
            ans1.append(y)
            ans2.append(x)
            ans2.append(y)
    print(*ans1)
    print(*ans2)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()

