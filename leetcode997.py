from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        array = [0] * (n + 1)
        for (a, b) in trust:
            array[a] -= 1
            array[b] += 1
        for i in range(1, len(array)):
            if array[i] == n - 1:
                return i
        return -1


import hypothesis
import hypothesis.strategies as st

Solution().findJudge(n=3, trust=[[1, 3], [2, 3]])
