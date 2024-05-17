S = lambda: map(int, input().split())
L = lambda: list(S())

import sys

def query(a, b):
    qt = "? " + str(a) + " " + str(b)
    sys.stdout.write(qt + '\n')
    sys.stdout.flush()
    return

def anssub(a, b):
    qt = "! " + str(a) + " " + str(b)
    sys.stdout.write(qt + '\n')

def solve():
    n, k = S()
    
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()