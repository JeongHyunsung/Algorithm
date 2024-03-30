S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    x = input()
    ans = []
    low = []
    upper = []
    cnt = 0
    for i in x:
        if i == "b":
            if ans:
                if low:
                    ans[low.pop()] = "0"
        elif i == "B":
            if ans:
                if upper:
                    ans[upper.pop()] = "0"
        else:
            if 65<=ord(i)<=90:
                upper.append(cnt)
            else:
                low.append(cnt)
            ans.append(i)
            cnt += 1
    for i in ans:
        if i != "0":
            print(i, end="")
    print()
    return

if __name__ == "__main__":
    for test in range(int(input())):
        solve()
