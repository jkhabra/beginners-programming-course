from algorithms import selection_sort, bubble_sort, merge_sort

ls1 = [2, 5, 6, 7, 8, 1]
ls2 = [1]
ls3 = [3, 4, 6, 7, 2, 89, 2]
ls4 = [10, 55, 4, 99, 90, 29, 1, 990]
ls5 = []


def test_selection_sort():
    assert selection_sort(ls1) == sorted(ls1)
    assert selection_sort(ls2) == sorted(ls2)
    assert selection_sort(ls3) == sorted(ls3)
    assert selection_sort(ls4) == sorted(ls4)
    assert selection_sort(ls5) == sorted(ls5)


def test_bubble_sort():
    assert bubble_sort(ls1) == sorted(ls1)
    assert bubble_sort(ls2) == sorted(ls2)
    assert bubble_sort(ls3) == sorted(ls3)
    assert bubble_sort(ls4) == sorted(ls4)
    assert bubble_sort(ls5) == sorted(ls5)


def test_merge_sort():
    assert merge_sort(ls1) == sorted(ls1)
    assert merge_sort(ls2) == sorted(ls2)
    assert merge_sort(ls3) == sorted(ls3)
    assert merge_sort(ls4) == sorted(ls4)
    assert merge_sort(ls5) == sorted(ls5)
