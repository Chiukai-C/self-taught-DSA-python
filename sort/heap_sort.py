def sift(heap, low, high):
    i = low
    j = 2 * i + 1
    while j <= high:
        if j + 1 <= high and heap[j] < heap[j + 1]:
            j = j + 1
        if heap[j] > heap[i]:
            heap[i], heap[j] = heap[j], heap[i]
            i = j
            j = 2 * i + 1
        else:
            break
    return


def heap_sort(li):
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):
        sift(li, i, n - 1)
    while n > 1:
        li[0], li[n - 1] = li[n - 1], li[0]
        sift(li, 0, n - 2)
        n -= 1
    return li


# test 1:
print(heap_sort([2, 6, 7, 3, 4, 11, 5, 8, 9, 1, 10]))
# time complexity: O(n*log(n)))

