from typing import Optional,List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        ### dict count solution
        
        # my_counter = Counter(nums)
        # count = 0
        # for key in list(my_counter):
        #     if k-key in my_counter.keys():
        #         if k-key == key:
        #             count+=(my_counter[k-key]//2)
        #         else:
        #             count+=min(my_counter[k-key],my_counter[key])
                
        #         del my_counter[k-key]

        # return count            
        
        
        ### Left and right pointer solution
        
        nums.sort()
        n = len(nums)
        left, right, count = 0, n-1, 0
        
        while left<right:
            s = nums[left]+nums[right]
            if s==k:
                count+=1
                left+=1
                right-=1
            elif s<k:
                left+=1
            else:
                right-=1
        
        return count

if __name__ == "__main__":
    
    nums = [2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2]
    k = 3
    
    # nums = [3,1,3,4,3]
    # k = 6
    
    # nums = [1,2,3,4]
    # k = 5
    
    print(Solution().maxOperations(nums,k))