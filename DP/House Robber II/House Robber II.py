from typing import List


def rob(nums: List[int]) -> int:
    def helper(nums):
        a = 0
        b = 0
        for i in nums:
            a, b = b, max(a + i, b)
        return b

    if (len(nums) <= 3):
    #for <4 elements, the max sum is 1 of the 3 houses
        return max(nums)
    return max(helper(nums[:len(nums) - 1]), helper(nums[1:len(nums)]))