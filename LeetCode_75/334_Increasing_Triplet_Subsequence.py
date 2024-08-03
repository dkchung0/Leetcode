from typing import Optional,List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        # for i in range(len(nums)-2):
        #     p1,p2,p3 = i,i+1,i+2
        #     while p1 < p2 and p2 < p3 and p3 < len(nums):
        #         if nums[p2] > nums[p1] and nums[p3] > nums[p2]:
        #             return True
        #         elif nums[p1] > nums[p2]:
        #             p2+=1
        #             p3+=1
        #         elif nums[p2] > nums[p3]:
        #             p3+=1
                
        # return False
        
        # 追蹤目前找到的最小值和第二小值
        first = second = float('inf')

        for n in nums:
            '''
            # 當第二個比第一個小，這時就代表從第二個開始。
            '''
            if n <= first:
                # 當前元素比 first 還小或等於時，更新 first
                first = n
            elif n <= second:
                # 當前元素比 first 大，但比 second 小或等於時，更新 second
                second = n
            else:
                # 當前元素比 first 和 second 都大時，說明找到了遞增的三元子序列
                return True
                
        return False
        
            
if __name__== '__main__':
    
    # nums = [50,20,100,10,12,1]
    nums = [2,1,5,0,4,1,3]
    print(Solution().increasingTriplet(nums))
    