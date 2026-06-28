class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        array_to_list = {}
        for word in strs:
            curr = [0] * 26 

            for char in word: 
                idx = ord(char) - 96
                curr[idx -1] += 1
            
            curr_tuple = tuple(curr)

            if curr_tuple in array_to_list: 
                array_to_list[curr_tuple].append(word)
            else: 
                array_to_list[curr_tuple] = [word]
        
        # create a output list 
        res = []
        for k, v in array_to_list.items():
            res.append(v)
        
        return res