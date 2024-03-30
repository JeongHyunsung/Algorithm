S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = input()
    ref = []
    for i in range(10):
        ref.append((i+1)+(i+1)*(i)/2)
    ans = 1
    for i in n:
        ans *= ref[int(i)]
    print(int(ans))
    return

if __name__ == "__main__":
    for test in range(int(input())):
        solve()
