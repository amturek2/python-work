class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean 
            # lowercase
            # remove space
        clean = ""
        s = s.lower()
        for l in s: 
            if l.isalpha() or l.isnumeric():
                clean = clean+l 
     

        # do a two pointer search front to back 
            # false if back pointer doesnt equal front pointer

        l, r = 0, len(clean) -1

        while l <= r: 
            if clean[l] != clean[r]:
                return False
            l += 1
            r -= 1

        return True
        # Time Complexity: O(n)
        # Space Complexity: O(n)
