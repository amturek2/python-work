class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: 
            num = len(s)
            res += str(num)
            res += "#"
            res += s

        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        # we will go through each letter 
        # once we find an #
        # look at int before hashtag
        # add the next __ letters to the map 
        i = 0
        while i < len(s): 
            j = i 
            while s[j] != "#":
                j+= 1
     
            length = int(s[i:j])
            start = j+1
            end = j + length + 1
            word = s[start:end]
            i = end
            res.append(word)



        return res
