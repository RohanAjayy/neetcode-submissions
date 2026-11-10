class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # seen = { 4:0, 5:1, 6:2}
        # nums = [3,4,5,6]
        seen = {} 
        for i, num in enumerate(nums): # {[0,3], [1,4], [2,5], [3,6]...}
                                     #   i s    
            diff = target - num
            # 4
            if diff in seen:
                return [seen[diff], i] 
            
            seen[num] = i
            
        return []