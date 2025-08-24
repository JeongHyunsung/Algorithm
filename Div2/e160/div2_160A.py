S = lambda : map(int, input().split())
L = lambda : list(S())


def solve():
    s = input()
    solved = 0
    if s[0] == "0":
        print(-1)
        return
    for i in range(len(s)-1):
        if s[i+1] != "0":
            a = s[:i+1]
            b = s[i+1:]
            a = int(a)
            b = int(b)
            if a < b and a > 0 and b > 0:
                solved = 1
                break
    if solved:
        print(a, b)
    else:
        print(-1)



    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
