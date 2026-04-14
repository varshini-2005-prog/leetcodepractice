class Solution:
    def minimumTotalDistance(self, robot, factory):

        robot.sort()
        factory.sort()

        f = []
        for p, l in factory:
            for i in range(l):
                f.append(p)

        n = len(robot)
        m = len(f)

        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

        for j in range(m + 1):
            dp[0][j] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                dp[i][j] = dp[i][j-1]

            
                if dp[i-1][j-1] != float('inf'):
                    cost = dp[i-1][j-1] + abs(robot[i-1] - f[j-1])
                    dp[i][j] = min(dp[i][j], cost)

        return dp[n][m]