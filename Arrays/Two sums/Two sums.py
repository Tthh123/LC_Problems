from typing import List
def twoSum(self, nums: List[int], target: int) -> List[int]:
    dict = {}
    for index, num in enumerate(nums):
        if (target - num) in dict:
            return [index, dict[target - num]]
        else:
            dict[num] = index