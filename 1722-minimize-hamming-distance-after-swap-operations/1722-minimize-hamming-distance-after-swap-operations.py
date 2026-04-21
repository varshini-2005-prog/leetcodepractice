class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        parent = list(range(len(source)))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa != pb:
                parent[pb] = pa
        
        for a, b in allowedSwaps:
            union(a, b)
        
        from collections import defaultdict
        groups = defaultdict(list)
        
        for i in range(len(source)):
            root = find(i)
            groups[root].append(i)
        
        mismatch = 0
        
        for group in groups.values():
            count = {}
            
            for i in group:
                count[source[i]] = count.get(source[i], 0) + 1
            
            for i in group:
                if count.get(target[i], 0) > 0:
                    count[target[i]] -= 1
                else:
                    mismatch += 1
        
        return mismatch