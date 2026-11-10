class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        # nums = [3,4,5,6]
        # seen = {4, } 
        for i, s in enumerate(nums): # {[0,3], [1,4] ...}
            diff = target - s
            
            if diff in seen:
                return [seen[diff], i] 
            else:
                seen[s] = i
            
        return []