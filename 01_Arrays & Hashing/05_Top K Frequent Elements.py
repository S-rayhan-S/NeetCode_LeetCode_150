from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict=defaultdict(int)
        for i in nums:
            freq_dict[i] +=1 
            # +count.get(i,0)

        list_arr=[[] for _ in range(len(nums)+1)]
        
        for key,val in freq_dict.items():
            list_arr[val].append(key)

        copy_k=k
        ans_list=[]
        for i in range(len(list_arr)-1,0,-1):
            for j in list_arr[i]:
                ans_list.append(j)
                if len(ans_list)==k:
                    return ans_list
                













