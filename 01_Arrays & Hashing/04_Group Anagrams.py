## My soln: O(m*n*log(n)) ; 
## n is the largest str size, m is ttl no of str
class Solution:
    
    str_dict = {}
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        for i in strs:
            # sorted returns a list & list is not hashable ,
            # thus need to convert to tuple to make ihashable to use as a key
            key=tuple(sorted(i)) 
            if key not in str_dict:
                str_dict[key]=[]
            str_dict[key].append(i)
        return list(str_dict.values())

## Optimized soln:
## use frequency array instead
class Solution:
    # from collections import defaultdict , this line can initialize dictionary with empty list
    # list are mutable so can't be used as key.instead convert to tule

    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        for stri in strs:
            freq_cnt=[0]*26
            for ch in stri:
                freq_cnt[ord(ch)-ord('a')]+=1
            str_dict.setdefault(tuple(freq_cnt),[]).append(stri)
        return  list(str_dict.values())






