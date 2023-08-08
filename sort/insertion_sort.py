def insertion_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        while i > 0 and li[i - 1] > tmp:
            li[i] = li[i - 1]
            i -= 1
        li[i] = tmp
    return li


# test:
print(insertion_sort([2, 6, 7, 3, 4, 11, 5, 8, 9, 1, 10]))
# time complexity: O(n**2))

