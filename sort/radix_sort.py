import random


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


li = [random.randint(0, 100000000) for _ in range(10000)]
print(li)
print(radix_sort(li))
# average time complexity: O(nk) (k is the number of digits)
# space complexity: O(n+k)

