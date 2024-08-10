from typing import Optional,List
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2) or  set(word1) != set(word2):
            return False
        
        return sorted(Counter(word1).values()) == sorted(Counter(word2).values())

if __name__== '__main__':
    
    word1 = "abbzccca"
    word2 = "babzzczc"
    print(Solution().closeStrings(word1,word2))
    