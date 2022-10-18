# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        list3 = head
        
        while list1 or list2:
            if list1 and list2:
                list3.next = list1 if list1.val < list2.val else list2

                if list1.val < list2.val:
                    list1 = list1.next
                else:
                    list2 = list2.next
            elif list1:
                list3.next = list1
                break
            elif list2:
                list3.next = list2
                break
            list3 = list3.next
        return head.next
        