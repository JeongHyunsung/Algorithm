S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    s = input()
    counter = {}
    for i in s:
        if i in counter.keys():
            counter[i] += 1
        else:
            counter[i] = 1
    counter = sorted(counter.items(), key = lambda x: x[1], reverse=True)
    _, ans = counter[0]
    if ans > n-ans:
        print(2*ans-n)
    else:
        if n % 2 == 1:
            print(1)
        else:
            print(0)
    return

if __name__ == "__main__":
    for test in range(int(input())):
        solve()
