def partition(li, left, right):
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


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)
    return li


# test 1:
print(quick_sort([2, 6, 7, 3, 4, 11, 5, 8, 9, 1, 10], 0, 10))
# time complexity: O(n*log(n)))

