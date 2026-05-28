class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        for i in range(len(s2)-k+1):
            sub=s2[i:i+k]
            if sorted(sub)==sorted(s1):
                return True
                break
        return False