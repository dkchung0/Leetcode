from typing import Optional,List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        sum_ = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            sum_-=nums[i]
            if left_sum==sum_:
                return i
                
            left_sum+=nums[i]
        
        return -1

if __name__== '__main__':
    
    nums = [1,7,3,6,5,6]
    print(Solution().pivotIndex(nums))