from typing import Optional,List
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        # queue = list(senate)
        # ans_dict = {
        #     'R':"Radiant",
        #     'D':"Dire"
        # }
        
        # temp=""
        # count= 0
        # while len(set(queue))!=1: # 時間複雜度高的主因
        #     if not temp:
        #          temp = queue[0]
            
        #     if queue[0] != temp :
        #         count-=1
        #     else:
        #         queue.append(queue[0])
        #         count+=1

        #     if count==0:
        #         temp = ""
            
        #     queue.pop(0)
        
        # return ans_dict[queue[0]]
        
         
        d_deque = deque(index_d for index_d,d in enumerate(senate) if d=="D")
        r_deque = deque(index_r for index_r,r in enumerate(senate) if r=="R")
        
        n = len(senate)
        while  d_deque and r_deque:
            cur_d = d_deque.popleft()
            cur_r = r_deque.popleft()
            
            if cur_d > cur_r:
                r_deque.append(n+cur_r)
            else:
                d_deque.append(n+cur_d)
            
        return "Dire" if d_deque else "Radiant"

if __name__== '__main__':
    
    senate = "DDRRR"
    # Output: "Dire"
    
    print(Solution().predictPartyVictory(senate))