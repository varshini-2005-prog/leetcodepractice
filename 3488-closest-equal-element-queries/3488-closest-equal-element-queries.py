class Solution:
    def solveQueries(self, nums, queries):
        n = len(nums)
        
        pos = {}
        
        for i in range(n):
            if nums[i] not in pos:
                pos[nums[i]] = []
            pos[nums[i]].append(i)
        
        index_map = {}
        for val in pos:
            arr = pos[val]
            for i in range(len(arr)):
                index_map[arr[i]] = i
        
        res = []
        
        for q in queries:
            arr = pos[nums[q]]
            
            if len(arr) == 1:
                res.append(-1)
                continue
            
            i = index_map[q]   
            m = len(arr)
            
            prev_i = (i - 1 + m) % m
            next_i = (i + 1) % m
            
            d1 = abs(arr[i] - arr[prev_i])
            d2 = abs(arr[i] - arr[next_i])
            
            d1 = min(d1, n - d1)
            d2 = min(d2, n - d2)
            
            res.append(min(d1, d2))
        
        return res