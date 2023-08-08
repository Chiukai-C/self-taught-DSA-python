def binary_search(li, obj):
    left = 0
    right = len(li) - 1
    while left <= right:
        index = round((left + right) / 2)
        if li[index] == obj:
            return index
        elif li[index] < obj:
            left = index + 1
        else:
            right = index - 1
    else:
        return None


# test:
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
# time complexity: O(log(n))
