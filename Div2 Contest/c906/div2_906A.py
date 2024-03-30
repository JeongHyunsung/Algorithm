S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    counter = {}
    n = int(input())
    a = L()
    for i in a:
        if i not in counter.keys():
            counter[i] = 1
        else:
            counter[i] += 1
    k = list(counter.keys())
    if len(counter) == 1:
        print("Yes")
    elif len(counter) == 2:
        if abs(counter[k[0]] - counter[k[1]]) <= 1:
            print("Yes")
        else:
            print("No")
    else:
        print('No')
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
