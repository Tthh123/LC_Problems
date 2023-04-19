from typing import List
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers) - 1
    while (l < r):
        mid = (numbers[l] + numbers[r])
        if mid == target:
            return [l + 1, r + 1]
        if mid > target:
            r = r - 1
        else:
            l = l + 1