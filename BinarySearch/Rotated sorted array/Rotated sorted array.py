from typing import List
def search(nums: List[int], target: int) -> int:
    if len(nums) == 0:
        return -1
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[l] <= nums[mid]:
            if target >= nums[l] and nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if target >= nums[mid] and nums[r] >= target:
                l = mid + 1
            else:
                r = mid - 1
    return -1
print(search([3,1],1))