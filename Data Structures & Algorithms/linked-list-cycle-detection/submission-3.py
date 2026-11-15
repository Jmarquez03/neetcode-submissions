# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        check = head
        while check and check.next:
            check = check.next.next
            if check == head:
                return True
            head = head.next
        return False
        