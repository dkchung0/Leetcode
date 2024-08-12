from typing import Optional,List

class Solution:
    def decodeString(self, s: str) -> str:
        
        stack_list = []
        for i in s:
            if i == "]":
                temp_s = ""
                while stack_list and stack_list[-1] != "[":
                    temp_s = stack_list.pop(-1) + temp_s
                stack_list.pop(-1)  
                
                temp_n = ""
                while stack_list and stack_list[-1].isdigit():
                    temp_n = stack_list.pop(-1) + temp_n
         
                ans = temp_s * int(temp_n)
                stack_list.append(ans)
                    
            else:
                stack_list.append(i)
        
        return "".join(stack_list)
        
        
if __name__== '__main__':
    
    # s = "2[abc]3[cd]ef"
    # #Output: "abcabccdcdcdef"
    
    s = "3[a2[c]]"
    # #Output: "accaccacc"
    
    print(Solution().decodeString(s))