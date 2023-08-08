import random
from cal_time import cal_time


"""
heap_sort
"""


def sift(li, low, high):
    i = low
    j = 2 * i + 1
    while j <= high:
        if j + 1 <= high and li[j] > li[j + 1]:
            j += 1
        if li[i] > li[j]:
            li[i], li[j] = li[j], li[i]
            i = j
            j = 2 * i + 1
        else:
            break
    return


@cal_time
def top_k_heap(li, k):
    heap = li[:k]
    for i in range((k - 2) // 2, -1, -1):
        sift(heap, i, k - 1)
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k - 1)
    for i in range(k-1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    return heap


li = list(range(1000000))
random.shuffle(li)
print(top_k_heap(li, 2000))


"""
insertion_sort
"""


@cal_time
def top_k_insertion(li, k):
    for i in range(1, k):
        tmp = li[i]
        while i >= 1 and li[i - 1] < tmp:
            li[i] = li[i - 1]
            i -= 1
        li[i] = tmp
    for i in range(k, len(li)):
        if li[i] > li[k - 1]:
            li[k - 1] = li[i]
        i = k - 1
        tmp = li[i]
        while i >= 1 and li[i - 1] < tmp:
            li[i] = li[i - 1]
            i -= 1
        li[i] = tmp
    return li[:k]


li = list(range(1000000))
random.shuffle(li)
print(top_k_insertion(li, 2000))
