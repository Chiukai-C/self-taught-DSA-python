def bisect_right(arr, target):
    beg, end = 0, len(arr) - 1
    while beg <= end:
        mid = (beg + end) // 2
        if arr[mid] <= target:
            beg = mid + 1
        else:
            end = mid - 1
    return beg


# test 1:
print(bisect_right([1,  2,  2,  2,  3,  7,  7,  9], 2))  # 4
# test 2:
print(bisect_right([1,  2,  2,  2,  3,  7,  7,  9], 5))  # 5
# test 3:
print(bisect_right([1, 2, 3], 0))  # 0
# test 4:
print(bisect_right([1, 2, 3], 4))  # 3
# test 5:
print(bisect_right([1], 1))  # 1
