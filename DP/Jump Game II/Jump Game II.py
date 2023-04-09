def jump(nums) -> int:
    jumps = 0
    l = r = 0
    while (r < len(nums) - 1):
        maxr=0
        for i in range(l,r+1):
            #Adding of index to number to find max window size
            maxr=max(maxr,nums[i]+i)
        l, r = r + 1, maxr
        jumps=jumps+1
    return jumps
print(jump([3,4,3,2,5,4,3]))
