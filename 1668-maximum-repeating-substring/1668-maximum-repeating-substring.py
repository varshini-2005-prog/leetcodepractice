class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)

        dp = [0]*(n+1)
        ans=0
        for i in range(m,n+1):
            if sequence[i-m:i]==word:
                dp[i] = dp[i-m] + 1
            ans = max(ans,dp[i])
        return ans
