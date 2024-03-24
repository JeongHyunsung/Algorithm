S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n, k = S()
    st = input()
    counter = [0]*(ord("z")-ord("a")+1)
    for ch in st:
        counter[ord(ch) - ord("a")] += 1
    o = 0
    for i in counter:
        if i % 2 == 1:
            o += 1
    if k >= o-1:
        print("YES")
    else:
        print("NO")

    
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()

