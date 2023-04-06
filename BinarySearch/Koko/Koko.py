from typing import List
from math import ceil


def minEatingSpeed(piles: List[int], h: int) -> int:
    if (h == len(piles)):
        return max(piles)
    l = 1
    r = max(piles)
    while (l <= r):
        totaltime = 0
        k = (l + r) // 2
        for i in piles:
            if (k >= i):
                totaltime = totaltime + 1
            else:
                totaltime = totaltime + ceil(i / k)
        if (totaltime <= h):
            r = k - 1
        else:
            l = k + 1
    return k


print(minEatingSpeed([30,11,23,4,20],6))