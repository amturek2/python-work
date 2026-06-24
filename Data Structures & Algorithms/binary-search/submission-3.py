class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binsearch(nums, 0, len(nums) - 1, target)
    

    def binsearch(self, nums: List[int], begin: int, end: int, target: int) -> int:

        mid = (begin + end) // 2
        midval = nums[mid]

        if target == midval: 
            
            return mid 
        if begin >= end: 
            return -1 
        if target == midval: 
            return mid 
        if target > midval: 
            return self.binsearch(nums, mid+1, end, target)
        
        return self.binsearch(nums, begin, mid, target)

