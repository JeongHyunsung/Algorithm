import sys
S = lambda: map(int, input().split())
L = lambda: list(S())


def query(a, b):
    qt = "? " + str(a) + " " + str(b)
    sys.stdout.write(qt + '\n')
    sys.stdout.flush()
    return

def anssub(a, b):
    qt = "! " + str(a) + " " + str(b)
    sys.stdout.write(qt + '\n')
