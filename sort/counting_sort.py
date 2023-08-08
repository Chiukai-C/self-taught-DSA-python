import random


def counting_sort(li, low, high):
    count = dict(zip(range(low, high+1), [0] * (high+1-low)))
    for val in li:
        count[val] += 1
    li.clear()
    for i, j in count.items():
        for _ in range(j):
            li.append(i)
    return li


# test 1:
li = [random.randint(0, 100000000) for _ in range(10000)]
print(li)
print(counting_sort(li, 0, 100000000))
# time complexity: O(n))
