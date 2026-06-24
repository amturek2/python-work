class Solution:
    def isValid(self, s: str) -> bool:
        backToFront = {")" : "(", 
                        "}" : "{", 
                        "]" : "[", }

        stack = []

        for c in s:
            if c in backToFront: 
                if len(stack) >0 and stack[-1] == backToFront[c]: 
                    stack.pop()
                else:
                   return False
            else: 
                stack.append(c)

        return (len(stack) == 0)