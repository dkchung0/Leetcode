from typing import Optional,List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ### change position solution
        
        # z_index = []
        # for index , i in enumerate(nums):
        #     if i == 0:
        #         z_index.append(index)
        #     else:
        #         if z_index:
        #             z = z_index.pop(0)
        #             nums[index] , nums[z] = nums[z] , nums[index]
        #             z_index.append(index)
                
        # return nums
        
        ### Move non-zero values ​​first solution
        
        index = 0
        for i in nums:
            if i!=0:
                nums[index] = i
                index+=1
        
        for j in range(index,len(nums)):
            nums[j] = 0
            
        return nums
            

if __name__ == "__main__":
    
    nums = [0,1,0,3,12]
    print(Solution().moveZeroes(nums))