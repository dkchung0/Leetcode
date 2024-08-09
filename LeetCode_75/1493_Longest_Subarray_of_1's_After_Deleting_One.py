from typing import Optional,List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        if sum(nums) == n:
            return n - 1
        
        left , right = 0 , 0
        res_sum=0
        for i in range(n):
            if nums[i]==0:
                # caculate Previous zero
                res_sum = max(res_sum,left+right)
                left=right
                right=0
            else:
                right+=1

        # avoid last one not zero
        res_sum = max(res_sum,left+right)
        
        return res_sum

    
if __name__== '__main__':
    
    nums = [0,1,1,1,0,1,1,0,1]
    print(Solution().longestSubarray(nums))