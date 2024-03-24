import sys
S = lambda: map(int, input().split())
L = lambda: map(list(S()))

def query(a, b, c, d):
    qt = "? "+str(a)+" "+str(b)+" "+str(c)+" "+str(d)
    sys.stdout.write(qt + '\n')
    sys.stdout.flush()
    return

def anssub(a, b):
    qt = "! "+str(a)+" "+str(b)
    sys.stdout.write(qt + '\n')

def solve():
    n = int(input())
    if n == 2:
        anssub(0, 1)
        return
    query(0, 0, 1, 1)
    winner = -1
    if input() == "<":
        winner = 1
    else:
        winner = 0
    for i in range(2, n):
        query(winner, winner, i, i)
        if input() == "<":
            winner = i

    cand = list(range(n))
    cand.remove(winner)

    m_cand = []
    query(winner, cand[0], winner, cand[1])
    x = input()
    if x == "<":
        m_cand.append(cand[1])
    elif x == ">":
        m_cand.append(cand[0])
    else:
        m_cand.append(cand[0])
        m_cand.append(cand[1])

    for i in range(2, len(cand)):
        query(winner, m_cand[0], winner, cand[i])
        x = input()
        if x == "<":
            m_cand = [cand[i]]
        elif x == "=":
            m_cand.append(cand[i])

    loser = -1

    if len(m_cand) == 1:
        loser = m_cand[0]
    else:
        query(m_cand[0], m_cand[0], m_cand[1], m_cand[1])
        if input() == "<":
            loser = m_cand[0]
        else:
            loser = m_cand[1]
        for i in range(2, len(m_cand)):
            query(loser, loser, m_cand[i], m_cand[i])
            if input() == ">":
                loser = m_cand[i]
    anssub(winner, loser)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
