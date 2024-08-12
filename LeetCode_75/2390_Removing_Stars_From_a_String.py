from typing import Optional,List

class Solution:
    def removeStars(self, s: str) -> str:
        
        stack_list = []
        for i in s:
            if i != "*":
                stack_list.append(i)
            else:
                stack_list.pop(-1)
        
        return "".join(stack_list)        


if __name__== '__main__':
    
    s = "leet**cod*e"
    print(Solution().removeStars(s))
