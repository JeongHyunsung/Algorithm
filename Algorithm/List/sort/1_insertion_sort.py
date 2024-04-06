def insertion_sort(l):
    # average case time complexity: n^2
    # worst case time complexity: n^2
    # best case time complexity: n
    for i in range(len(l)):
        j = i
        while j > 0 and l[j] < l[j-1]:
            m = l[j]
            l[j] = l[j-1]
            l[j-1] = m
            j -= 1
    return

l = [0, 34, 2, 30, 5, 20, 14, 15, 84, 3]
insertion_sort(l)

print(l)