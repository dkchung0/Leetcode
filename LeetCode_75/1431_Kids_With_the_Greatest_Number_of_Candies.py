from typing import Optional,List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        return [i+extraCandies>=max(candies) for i in candies]
        


if __name__== '__main__':
    
    candies = [2,3,5,1,3]
    extraCandies = 3
    
    print(Solution().kidsWithCandies(candies,extraCandies))