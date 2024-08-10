from typing import Optional,List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        return len(set(Counter(arr).values())) == len(set(arr))



if __name__== '__main__':
    
    arr = [1,2,2,1,1,3]
    print(Solution().uniqueOccurrences(arr))