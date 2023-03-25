from typing import List
from math import floor,ceil


def minEatingSpeed(piles: List[int], h: int) -> int:
    #edge case whereby len of list == hours, in this case min no of bananas per hour is the same as the max
    if (h == len(piles)):
        return max(piles)
    l = 1
    r = max(piles)
    minno = r#need to save the minimum no of bananas
    while (l <= r):#binary search between 1 and max in piles
        totaltime = 0
        k = (l + r) // 2
        for i in piles:
            if (k >= i):
                totaltime = totaltime + 1
            else:
                totaltime = totaltime + ceil(i / k)
        if (totaltime <= h):
            minno = min(minno, k)
            r = k - 1
        else:
            l = k + 1
    return minno


print(minEatingSpeed([30,11,23,4,20],6))