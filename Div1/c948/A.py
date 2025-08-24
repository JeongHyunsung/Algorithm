S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    l = L()
    l.append(l[0])
    cnt = 0
    for i in range(n):
        if l[i+1] < l[i]:
            cnt += 1

    if cnt >= 2:
        print("NO")
    else:
        print("YES")
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()