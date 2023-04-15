def mySqrt(self, x: int) -> int:
    if (x < 2):
        return x
    l = 0
    r = x
    #binary search
    while (l < r):
        mid = (l + r) // 2
        if (mid * mid) == x:
            return mid
        elif (mid * mid) > x:
            r = mid
        else:
            l = mid + 1
    #Have to minus 1 for cases whereby X is not an integer hence we round down
    return l - 1