class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        res=[]
        for i in range(n+1):
            for j in range(i+1,len(s)+1):
                if s[i:j]==s[i:j][::-1]:
                    res.append(s[i:j])
        return len(res)