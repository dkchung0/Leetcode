from typing import Optional,List
from collections import defaultdict

class Solution:
    def compress(self, chars: List[str]) -> int:
        temp = chars[0]
        temp_num = 1
        index = 0
        
        for i in range(1, len(chars)):
            if chars[i] == temp:
                temp_num += 1
            else:
                chars[index] = temp
                index += 1
                if temp_num > 1:
                    for num in str(temp_num):
                        chars[index] = num
                        index += 1
                temp = chars[i]
                temp_num = 1
        
        chars[index] = temp
        index += 1
        if temp_num > 1:
            for num in str(temp_num):
                chars[index] = num
                index += 1
        
        return index
        
        
if __name__== '__main__':

    chars = ["a","a","a","b","b","a","a"]

    print(Solution().compress(chars))