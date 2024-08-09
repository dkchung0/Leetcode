from typing import Optional,List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        cur_alt, max_alt = 0, 0
        for g in gain:
            cur_alt+=g
            if g>0:
                max_alt = max(max_alt,cur_alt)
                
        return max_alt

if __name__== '__main__':
    
    gain = [-4,-3,-2,-1,4,3,2]
    #Output: 0
    
    gain = [-5,1,5,0,-7]
    #Output: 1
    
    print(Solution().largestAltitude(gain))