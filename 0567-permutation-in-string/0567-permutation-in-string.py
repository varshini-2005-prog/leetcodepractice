class Solution(object):
    def checkInclusion(self, s1, s2):
        need = Counter(s1)

        left = 0
        count = len(s1)

        for i in range(len(s2)):

            if need[s2[i]] > 0:
                count -= 1

            need[s2[i]] -= 1

            if i - left + 1 > len(s1):

                need[s2[left]] += 1

                if need[s2[left]] > 0:
                    count += 1

                left += 1

            if count == 0:
                return True

        return False