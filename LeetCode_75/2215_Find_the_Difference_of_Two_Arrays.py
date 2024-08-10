from typing import Optional,List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        
        return [list(nums1_set-nums2_set),list(nums2_set-nums1_set)]
    
    
if __name__== '__main__':
    
    nums1 = [1,2,3,3]
    nums2 = [1,1,2,2]
    #Output: [[3],[]]
    
    print(Solution().findDifference(nums1,nums2))

        