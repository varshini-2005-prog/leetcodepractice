class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        longest = ""

        for i in range(n):
            for j in range(i+1, n+1):
                sub = s[i:j]  
                letters = set(sub)
               
                nice = True
                for c in letters:
                    if c.swapcase() not in letters:
                        nice = False
                        break
                if nice and len(sub) > len(longest):
                    longest = sub

        return longest
