def selection_sort(ls):
    if len(ls) <= 1:
        return ls

    min_index = ls.index(min(ls))
    ls[0], ls[min_index] = ls[min_index], ls[0]

    return [ls[0]] + selection_sort(ls[1:])


def bubble_sort(ls):
    n = len(ls)

    for i in range(n - 1):
        for i in range(n - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
    return ls


def merge(left, right):
    """Join sorted lists left and right and returns new sorted list"""
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(ls):
    if len(ls) < 2:
        return ls

    mid = len(ls) // 2
    left = merge_sort(ls[:mid])
    right = merge_sort(ls[mid:])

    return merge(left, right)
