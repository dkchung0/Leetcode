from typing import Optional,List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        nn = len(flowerbed)
        for i in range(nn):
            if flowerbed[i]==0:
                prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
                next_empty = (i == nn - 1) or (flowerbed[i + 1] == 0)
            
                if prev_empty and next_empty:
                    flowerbed[i]=1
                    n-=1
                
        return n<=0
        
if __name__== '__main__':
    
    flowerbed = [1,0,0,0,0,1]
    n = 2
    
    print(Solution().canPlaceFlowers(flowerbed,n))