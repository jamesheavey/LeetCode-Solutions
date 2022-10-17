# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        start = result
        cumulative = 0
        
        while l1 or l2 or cumulative:
            if l1:
                cumulative += l1.val
                l1 = l1.next
            if l2:
                cumulative += l2.val
                l2 = l2.next
            result.next = ListNode(cumulative % 10)
            result = result.next
            cumulative //= 10
        
        return start.next
            
            