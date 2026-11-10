class Solution:
    def bullshit(self, string):
        seen = {}
        for char in string:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
        return seen

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        a = self.bullshit(s) 
        b = self.bullshit(t)
        if a == b:
            return True
    
        return False


















        # Normal Method
        # if len(s) != len(t):
        #     return False
        
        # seen = {}
        # a = list(s)
        # b = list(t)

        # a.sort()
        # b.sort()
        # if a == b:
        #     return True

        # return False