S = lambda: map(int, input().split())
L = lambda: list(S())

def solve():
    n = int(input())
    s = input()
    loc = {}
    for i in range(ord("a"), ord("z")+1):
        loc[chr(i)] = []
    for idx, i in enumerate(s):
        loc[i].append(idx)
    
    for i in range(ord("a"), ord("z")+1):
        loc[chr(i)].sort(reverse = True)
    max_chr = []
    min_chr = []
    cur_max, cur_min = "a", "z"
    for i in s[::-1]:
        if i > cur_max:
            cur_max = i
        max_chr.append(cur_max)
    max_chr.reverse()
    for i in s:
        if i < cur_min:
            cur_min = i
        min_chr.append(cur_min)

    valid = 1
    ans = 0
    rm = len(s)
    print(min_chr, max_chr)
    for i in range(ord("a"), ord("z")+1):
        print("IN", "_", i)
        if len(loc[chr(i)]):
            for j in loc[chr(i)]:
                print("conduct", "___", j)
                if j >= rm:
                    print("ignored")
                    continue
                if j==0:
                    min_left = "z"
                else:
                    min_left = min_chr[j-1]
                max_right = max_chr[j]
                if max_right > min_left:
                    print("invalid", max_right, " ", min_left)
                    valid = 0
                    rm = 0
                else:
                    print("valid", max_right, " ", min_left)
                    ans += 1
                    rm = j
    if valid:
        print(ans)
    else:
        print(-1)

                


    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()

