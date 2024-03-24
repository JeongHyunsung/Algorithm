S = lambda : map(int, input().split())
L = lambda : list(S())


def solve():
    s = input()
    ones, zeros = 0, 0
    for i in s:
        if i == "1":
            ones += 1
        else:
            zeros += 1
    ans = 0

    for i in s:
        if i == "1" and zeros > 0:
            zeros -= 1
            ans += 1
        elif i == "0" and ones > 0:
            ones -= 1
            ans += 1
        else:
            break
    print(len(s)-ans)
        



    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
