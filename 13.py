class Solution(object):
    def romanToInt(self, s):
        res=0
        D={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)):
            if i+1<len(s) and D[s[i]]<D[s[i+1]]:
                res-=D[s[i]]
            else:
                res+=D[s[i]]
        return res