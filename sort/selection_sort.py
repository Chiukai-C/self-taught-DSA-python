def selection_sort(li):
    for i in range(len(li) - 1):
        min_index = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_index]:
                min_index = j
        if i != min_index:
            li[i], li[min_index] = li[min_index], li[i]
    return li


# test:
print(selection_sort([2, 6, 7, 3, 4, 11, 5, 8, 9, 1, 10]))
# time complexity: O(n**2)
