def rob(nums) -> int:
    best = 0
    prev = 0
    #For each 'money' in house, check if it's better to take this house + 2 houses away or previous is better
    for i in nums:
        prev, best = best, max(i + prev, best)
    return best