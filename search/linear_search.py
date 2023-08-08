# search the index of object in a list
def linear_search(li, obj):
    for index, value in enumerate(li):
        if value == obj:
            return index
    return None


# test:
print(linear_search([5, 7, 13, 33, 11, 4, 8], 13))
# time complexity: O(n)
