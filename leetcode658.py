from hypothesis import given, strategies as st


def findClosestElements(arr: list[int], k: int, x: int) -> list[int]:
    def func(val):
        if val < x:
            return abs(val - x) - 0.5
        else:
            return abs(val - x)

    return list(sorted(list(sorted(arr, key=func))[:k]))

# @given(st.lists(st.integers()), st.integers(), st.integers())
# @given([1, 2, 3, 4, 5], 4, 3)
# def test_findClosestElements(arr: list[int], k: int, x: int):
#     assert findClosestElements(arr, k, x) == [1, 2, 3, 4]
#

def tests():
    assert findClosestElements([1, 2, 3, 4, 5], k=4, x=3) == [1, 2, 3, 4]
    assert findClosestElements([1, 2, 3, 4, 5], k=4, x=-1) == [1, 2, 3, 4]
