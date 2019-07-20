# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 递归
        if head is None or head.next is None:
            return head
        
        next = head.next;
        head.next = self.swapPairs(next.next);
        next.next = head;
        return next;
        


