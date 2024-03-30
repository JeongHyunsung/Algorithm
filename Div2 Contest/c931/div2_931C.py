import sys
S = lambda: map(int, input().split())
L = lambda: map(list(S()))

def query(a, b):
    qt = "? " + str(a) + " " + str(b)
    sys.stdout.write(qt + '\n')
    sys.stdout.flush()
    return

def anssub(a, b):
    qt = "! " + str(a) + " " + str(b)
    sys.stdout.write(qt + '\n')

def solve():
    n, m = S()
    query(1, 1)
    clue = int(input())
    px1, px2, py1, py2 = 0, 0, 0, 0
    if clue < n:
        px1 = 1+clue
        py1 = 1
    else:
        px1 = n
        py1 = 2+clue-n
    if clue < m:
        px2 = 1
        py2 = 1+clue
    else:
        px2 = 2+clue-m
        py2 = m
    query(px1, py1)
    clue = int(input())
    if clue % 2 == 0:
        px1 -= clue//2
        py1 += clue//2
        query(px1, py1)
        if int(input()) == 0:
            anssub(px1, py1)
            return
    query(px2, py2)
    clue = int(input())
    anssub(px2 + clue//2, py2 - clue//2)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
