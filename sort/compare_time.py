from cal_time import *
import random
import copy
import sys
sys.setrecursionlimit(10000)


@cal_time
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


@cal_time
def insertion_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        while i > 0 and li[i - 1] > tmp:
            li[i] = li[i - 1]
            i -= 1
        li[i] = tmp
    return li


@cal_time
def selection_sort(li):
    for i in range(len(li) - 1):
        min_index = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_index]:
                min_index = j
        if i != min_index:
            li[i], li[min_index] = li[min_index], li[i]
    return li


def partition(li, left, right):
    # To deal with the extreme situation: list(range(10000, 0, -1))
    # number = random.randint(left, right)
    # li[left], li[number] = li[number], li[left]
    temp = li[left]
    while left < right:
        while left < right and li[right] >= temp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= temp:
            left += 1
        li[right] = li[left]
    li[left] = temp
    return left


def _quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        _quick_sort(li, left, mid - 1)
        _quick_sort(li, mid + 1, right)
    return li


@cal_time
def quick_sort(li):
    _quick_sort(li, 0, len(li) - 1)
    return li

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


@cal_time
def heap_sort(li):
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):
        sift(li, i, n - 1)
    while n > 1:
        li[0], li[n - 1] = li[n - 1], li[0]
        sift(li, 0, n - 2)
        n -= 1
    return li


def merge(li, low, mid, high):
    i = low
    j = mid + 1
    tmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            tmp.append(li[i])
            i += 1
        else:
            tmp.append(li[j])
            j += 1
    while i <= mid:
        tmp.append(li[i])
        i += 1
    while j <= high:
        tmp.append(li[j])
        j += 1
    li[low:high+1] = tmp


def _merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        _merge_sort(li, low, mid)
        _merge_sort(li, mid+1, high)
        merge(li, low, mid, high)
    return li


@cal_time
def merge_sort(li):
    _merge_sort(li, 0, len(li) - 1)
    return li


@cal_time
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


@cal_time
def counting_sort(li, low, high):
    count = dict(zip(range(low, high+1), [0] * (high+1-low)))
    for val in li:
        count[val] += 1
    li.clear()
    for i, j in count.items():
        for _ in range(j):
            li.append(i)
    return li


@cal_time
def bucket_sort(li, low, high, n=100):
    buckets = [[] for i in range(n)]
    l = (high - low + 1) // n
    for val in li:
        ind = min((val - low) // l, n - 1)
        buckets[ind].append(val)
        i = len(buckets[ind]) - 1
        while i > 0 and buckets[ind][i-1] > buckets[ind][i]:
            buckets[ind][i-1], buckets[ind][i] = buckets[ind][i], buckets[ind][i-1]
            i -= 1
    li.clear()
    for buc in buckets:
        li += buc
    return li


@cal_time
def radix_sort(li):
    max_num = max(li)
    n = 0
    while 10 ** n <= max_num:
        buckets = [[] for _ in range(10)]
        for i in range(len(li)):
            val = li[i]
            digit = (val // 10 ** n) % 10
            buckets[digit].append(li[i])
        li.clear()
        for bucket in buckets:
            li.extend(bucket)
        n += 1
    return li


li = list(range(10000))
random.shuffle(li)
li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)
li3 = copy.deepcopy(li)
li4 = copy.deepcopy(li)
li5 = copy.deepcopy(li)
li6 = copy.deepcopy(li)
li7 = copy.deepcopy(li)
li8 = copy.deepcopy(li)
li9 = copy.deepcopy(li)
li10 = copy.deepcopy(li)
li11 = copy.deepcopy(li)


bubble_sort(li1)
insertion_sort(li2)
selection_sort(li3)
quick_sort(li4)
heap_sort(li5)
merge_sort(li6)
shell_sort(li7)
radix_sort(li8)
counting_sort(li9, 0, 10000)
bucket_sort(li10, 0, 10000)
radix_sort(li11)
