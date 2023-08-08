from cal_time import *
from random import randint


def bubble_sort(li):
    n = len(li)
    for i in range(n-1):
        exchange = False
        for j in range(n-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            return li
    return li


# test 1:
print(bubble_sort([2, 6, 7, 3, 4, 11, 5, 8, 9, 1, 10]))
# time complexity: O(n**2))

