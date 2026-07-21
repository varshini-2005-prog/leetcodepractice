class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        s = "1" + s + "1"
        total = s.count("1") - 2
        ans = total

        i = 1
        while i < len(s) - 1:
            if s[i] == "0":
                left = 0
                while i < len(s) and s[i] == "0":
                    left += 1
                    i += 1

                ones = 0
                while i < len(s) and s[i] == "1":
                    ones += 1
                    i += 1

                right = 0
                j = i
                while j < len(s) and s[j] == "0":
                    right += 1
                    j += 1

                if left > 0 and ones > 0 and right > 0:
                    ans = max(ans, total + left + right)
            else:
                i += 1

        return ans