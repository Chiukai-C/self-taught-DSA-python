def shell_sort(li):
    d = len(li) // 2
    while d > 0:
        for i in range(d, len(li)):
            tmp = li[i]
            while i >= d and li[i - d] > tmp:
                li[i] = li[i - d]
                i -= d
            li[i] = tmp
        d //= 2
    return li


# test 1:
print(shell_sort([2, 6, 7, 3, 4, 11, 5, 8, 9, 1, 10]))
