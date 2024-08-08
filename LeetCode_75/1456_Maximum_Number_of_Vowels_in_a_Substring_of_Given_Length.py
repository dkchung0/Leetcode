from typing import Optional,List

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a','e','i','o','u'}
        
        cur_n = sum(i in vowel for i in s[:k])
        res = cur_n
        left = s[0]
        for i in range(1+k-1,len(s)):
            if s[i] in vowel and left not in vowel: 
                cur_n+=1
                res = max(res,cur_n)
            elif left in vowel and s[i] not in vowel:
                cur_n-=1
            
            left=s[i-k+1]
            
        return res


if __name__== '__main__':
    
    s = "abciiidef"
    k = 3
    
    print(Solution().maxVowels(s,k))