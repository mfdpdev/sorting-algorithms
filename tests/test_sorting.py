from src.sorting import bubble_sort

def test_bubble_sort():
    assert bubble_sort([4,1,2,5,3]) == [1,2,3,4,5]
    assert bubble_sort([4,5,3,1,2]) == [1,2,3,4,5]
    assert bubble_sort([2,1,5,3,4]) == [1,2,3,4,5]
