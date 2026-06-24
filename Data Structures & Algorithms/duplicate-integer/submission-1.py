class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # add things to a set 
        # if it is contained in set, we return false 
        seen = set()
        for i in range(len(nums)): 
            if nums[i] in seen: 
                return True
            seen.add(nums[i])

        return False
