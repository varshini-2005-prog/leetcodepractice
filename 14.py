class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        res=""
        f=strs[0]
        l=strs[-1]

        for i in range(len(f)):
            if i<len(f) and f[i]==l[i]:
                res+=f[i]
            else:
                break
        return res