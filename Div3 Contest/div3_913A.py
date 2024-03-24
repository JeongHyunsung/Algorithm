S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    x = input()
    l = ["a", "b", "c", "d", "e", "f", "g", "h"]
    l.remove(x[0])
    for i in l:
        print(i+str(x[1]))
    for i in range(1, 9):
        if i != int(x[1]):
            print(x[0]+str(i))
    return

if __name__ == "__main__":
    for test in range(int(input())):
        solve()
