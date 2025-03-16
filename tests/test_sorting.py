from src.sorting import bubble_sort, merge_sort, selection_sort, insertion_sort

def test_bubble_sort():
    assert bubble_sort([]) == []
    assert bubble_sort([4,1,2,5,3]) == [1,2,3,4,5]
    assert bubble_sort([4,5,3,1,2]) == [1,2,3,4,5]
    assert bubble_sort([2,1,5,3,4]) == [1,2,3,4,5]

def test_selection_sort():
    assert selection_sort([]) == []
    assert selection_sort([4,1,2,5,3]) == [1,2,3,4,5]
    assert selection_sort([4,5,3,1,2]) == [1,2,3,4,5]
    assert selection_sort([2,1,5,3,4]) == [1,2,3,4,5]

def test_insertion_sort():
    assert insertion_sort([]) == []
    assert insertion_sort([4,1,2,5,3]) == [1,2,3,4,5]
    assert insertion_sort([4,5,3,1,2]) == [1,2,3,4,5]
    assert insertion_sort([2,1,5,3,4]) == [1,2,3,4,5]

def test_merge_sort():
    assert merge_sort([4,1,2,6,5,3]) == [1,2,3,4,5,6]
    assert merge_sort([4,5,3,1,2]) == [1,2,3,4,5]
    assert merge_sort([2,1,5,3,4]) == [1,2,3,4,5]
    assert merge_sort([1]) == [1]
    assert merge_sort([]) == []
