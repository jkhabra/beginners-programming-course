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
