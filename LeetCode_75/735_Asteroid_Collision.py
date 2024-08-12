from typing import Optional,List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack_list = []  
        for i in asteroids:
            while stack_list and i < 0 < stack_list[-1]:
                if stack_list[-1] + i < 0 :
                    stack_list.pop(-1)
                elif stack_list[-1] + i == 0 :
                    stack_list.pop(-1)
                    break
                else:
                    break
            else:
                stack_list.append(i)
                            
        return stack_list


if __name__== '__main__':
    
    asteroids = [1,-2,-2,-2]
    print(Solution().asteroidCollision(asteroids))