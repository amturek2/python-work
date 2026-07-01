class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # need to be aware of ending in 9 - if you end in 9 update all previous 
        if digits[-1] != 9: 
            digits[-1] += 1
            return digits 

        if (len(digits) <= 1): 
            return [1,0]

        i = len(digits) -1
        print(i)
        while (digits[i] == 9 and i >0): 
            digits[i] = 0 
            if (digits[i - 1] != 9):
                digits[i - 1] += 1
                return digits
            i-=1 

        digits[0] = 0
        digits.insert(0, 1)
        return digits