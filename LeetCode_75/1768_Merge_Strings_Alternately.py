class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        n = min(len(word1),len(word2))
        ans = "".join(word1[i]+word2[i] for i in range(n))
        
        return ans+word1[n:] if len(word1)>n else ans+word2[n:]
        
        
if __name__== '__main__':
    
    word1 = "abc"
    word2 = "pqr"
    
    print(Solution().mergeAlternately(word1,word2))
    


 