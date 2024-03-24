S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n, m = S()
    s = input()
    t = input()
    zc, oc = 0, 0
    ct = 0
    for i in range(n-1):
        if s[i] == s[i+1] == "0":
            zc = 1
        elif s[i] == s[i+1] == "1":
            oc = 1
    for i in range(m-1):
        if t[i] == t[i+1] == "0" or t[i] == t[i+1] == "1":
            ct = 1
    
    if zc + oc == 2:
        print("NO")
    elif zc == 1:
        if t[0] == t[-1] == "1" and ct == 0:
            print("YES")
        else:
            print("NO")
    elif oc == 1:
        if t[0] == t[-1] == "0" and ct == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")

    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
