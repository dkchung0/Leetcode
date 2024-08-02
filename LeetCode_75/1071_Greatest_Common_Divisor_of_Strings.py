import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        n = math.gcd(len(str1),len(str2))

        return str1[:n] if str1+str2 == str2+str1 else ""
        
    
if __name__== '__main__':
    
    str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
    str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
    
    print(Solution().gcdOfStrings(str1,str2))