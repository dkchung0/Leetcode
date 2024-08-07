from typing import Optional,List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        cur_sum = sum(nums[:k])
        res = cur_sum
        for i in range(1,len(nums)-k+1):
            cur_sum = cur_sum - nums[i-1] + nums[i+k-1]
            res = max(res,cur_sum)
            
        return round(res/k,5)

if __name__=="__main__":
    
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(Solution().findMaxAverage(nums,k))