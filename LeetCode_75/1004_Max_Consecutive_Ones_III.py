from typing import Optional,List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left = 0 
        ans = sum(nums[:k])
        cur_m = k
        res = cur_m
        
        for i in range(k,len(nums)):
            '''
            step1 判斷當前是不是1
            step2 當前是0的話 先判斷加的話會不會超過k
            step3 再判斷最左邊是不是1 是的話迴圈移動left point
            '''
            
            if nums[i] == 1:
                ans+=1
                cur_m+=1
            else:
                if cur_m - ans <k:
                    cur_m+=1
                else:
                    while nums[left] ==1:
                        ans-=nums[left]
                        left+=1
                        cur_m-=1
    
                    left+=1
        
            res = max(res,cur_m)  
        
        return res
        
if __name__== '__main__':
    
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    
    print(Solution().longestOnes(nums,k))