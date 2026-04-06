class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split()
        m=s[-1]
        return len(m)