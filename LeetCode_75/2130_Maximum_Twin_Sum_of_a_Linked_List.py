from typing import Optional,List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # slow, fast = head, head
        # prev = None

        # while fast and fast.next:
        #     fast = fast.next.next

        #     tmp = slow.next
        #     slow.next = prev
        #     prev = slow
        #     slow = tmp
        
        # maxSum = 0
        # while slow:
        #     maxSum = max(maxSum, prev.val + slow.val)
        #     slow = slow.next
        #     prev = prev.next

        slow , fast = head , head.next
        stack = [slow.val]
        max_ans = float("-inf")

        while slow.next and fast.next:
            slow = slow.next
            fast = fast.next.next
            stack.append(slow.val)
        
        while stack:
            slow = slow.next
            max_ans = max(max_ans,slow.val+stack.pop())

        return max_ans
        