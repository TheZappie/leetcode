from typing import List

import pandas as pd


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return pd.Series(nums1 + nums2).median()


result = Solution().findMedianSortedArrays(nums1=[1, 3], nums2=[2])
print(result)