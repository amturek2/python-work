class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # one solution, one guaranteed solution

        # first make a map of the input 
        valToIndex = {}
        for i in range(len(nums)): 
            valToIndex[nums[i]] = i

        # evaluate solution with for loop 

        for i in range(len(nums)): 
            need = target - nums[i] 
            if need in valToIndex and (valToIndex[need] != i): 
                second = valToIndex[need]
                return [i, second]

        return []

        # Time Complexity: O(n)
        # Space Complexity: O(n)        