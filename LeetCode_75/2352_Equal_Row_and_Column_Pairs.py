from typing import Optional,List
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0 
        for i in range(n):
            col = [grid[j][i] for j in range(n)]
            for g in grid:
                if col == g:
                    ans+=1

        return ans


if __name__== '__main__':
    
    grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    
    print(Solution().equalPairs(grid))