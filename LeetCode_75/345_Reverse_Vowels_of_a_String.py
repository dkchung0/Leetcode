from typing import Optional,List

class Solution:
    def reverseVowels(self, s: str) -> str:

        vowel = ['A','a','E','e','I','i','O','o','U','u']
        temp = [i for i in s if i in vowel] 

        ans=""
        for i in s:
            if i in vowel:
                ans+=temp.pop()
            else:
                ans+=i     

        return ans

if __name__== '__main__':

    s = "leetcode"
    #Output: "leotcede"

    print(Solution().reverseVowels(s))