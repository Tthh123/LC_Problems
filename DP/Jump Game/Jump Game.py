def canJump(nums)->bool:
    goal=len(nums)-1
    #backtracking
    for i in range(len(nums)-2,-1,-1):
        if (nums[i]+i)>=goal:
            goal=i
    return goal==0

print(canJump([1,2]))

# if (len(nums) == 1):
#     return True
# able = False
# s1 = 0
# s2 = 0
# for i in range(len(nums) - 1):
#     if (nums[i] == 0 and s2 <= i):
#         break
#     s1, s2 = s2, max(s2, i + nums[i])
#     if s2 >= (len(nums) - 1):
#         able = True
#
# return able