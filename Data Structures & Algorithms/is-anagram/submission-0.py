class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen = {}
        a = list(s)
        b = list(t)

        a.sort()
        b.sort()
        if a == b:
            return True






        # for i, s in enumerate(s):
        #     seen[s] = i

        # print(seen)

        return False