from typing import List

def minEatingSpeed(piles: List[int], h: int) -> int:
    def feasible(speed) -> bool:
        # return sum(math.ceil(pile / speed) for pile in piles) <= H  # slower
        sum=0
        for pile in piles:
            sum=sum+((pile)/speed)+1
        return sum<=h
        #return sum((pile - 1) / speed + 1 for pile in piles) <= h  # faster

    left, right = 1, max(piles)
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left


print(minEatingSpeed([30,11,23,4,20],6))