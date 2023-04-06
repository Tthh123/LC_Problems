def canJump(nums)->bool:
    if (len(nums) == 1):
        return True
    able = False
    s1 = 0
    s2 = 0
    for i in range(len(nums) - 1):
        if (nums[i] == 0 and s2 <= i):
            break
        s1, s2 = s2, max(s2, i + nums[i])
        if s2 >= (len(nums) - 1):
            able = True

    return able

print(canJump([2,3,1,1,4]))