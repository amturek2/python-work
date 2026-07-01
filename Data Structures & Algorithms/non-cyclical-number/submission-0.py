class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        value = self.squareEachAndAdd(self.splitToDigits(n))
        seen.add(value)
        while (value != 1): 
            print(value)
            value = self.squareEachAndAdd(self.splitToDigits(value))
            if value in seen: 
                return False
            seen.add(value)

        return True 
    def splitToDigits(self, n: int) -> []:
        res = []
        s = str(n)
        for c in s: 
            res.append(int(c))
        return res 

    def squareEachAndAdd(self, nums: []) -> int:
        res = 0
        for n in nums: 
            res += n ** 2
        return res



