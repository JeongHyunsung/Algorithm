S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    l = L()
    l.sort()
    m = l[0]
    m2 = -1
    flag = 0
    for i in l:
        if i % m and m2 == -1:
            m2 = i
        else:
            if (i % m) * (i % m2) != 0:
                flag = 1
    if flag:
        print("NO")
    else:
        print("YES")


    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()