def generate(self, numRows: int) -> List[List[int]]:
    dp = [[0] * (i + 1) for i in range(numRows)]
    dp[0][0] = 1
    # base case
    for n in range(1, numRows):
        dp[n][0] = 1
        dp[n][len(dp[n]) - 1] = 1
        for x in range(1, len(dp[n]) - 1):
            dp[n][x] = dp[n - 1][x - 1] + dp[n - 1][x]
    return dp