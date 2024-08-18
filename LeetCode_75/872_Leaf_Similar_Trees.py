from typing import Optional,List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(root:Optional[TreeNode],temp_list:List) -> List:
            '''
            list可變所以可以選擇不用去retrun，這邊return是為了最後的答案
            '''
            
            if not root: 
                return 

            if not root.left and not root.right:
                temp_list.append(root.val)
            else:
                dfs(root.left,temp_list)
                dfs(root.right,temp_list)

            return temp_list

        return dfs(root1,[]) == dfs(root2,[])