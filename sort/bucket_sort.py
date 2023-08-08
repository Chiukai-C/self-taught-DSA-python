import random


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


# test 1:
li = [random.randint(0, 100000000) for _ in range(10000)]
print(li )
print(bucket_sort(li, 0, 100000000))
# average time complexity: O(n+k)
# worst case time complexity: O(n**2*k)
# space complexity: O(nk)
