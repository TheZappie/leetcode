from typing import List


def slow(nums: List[int], target: int) -> List[int]:
    import itertools
    result = next(combination for combination in itertools.combinations(enumerate(nums), 2) if
                  sum([combination[0][1], combination[1][1]]) == target)
    return [result[0][0], result[1][0]]


def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {value: idx for idx, value in enumerate(nums)}
    value, idx = next([value, idx] for value, idx in hashmap.items() if
                      hashmap.get(target - value) and hashmap.get(target - value) != idx)
    return [idx, hashmap.get(target - value)]


twoSum(nums=[2, 7, 11, 15], target=9)
twoSum(nums=[3, 3], target=6)
