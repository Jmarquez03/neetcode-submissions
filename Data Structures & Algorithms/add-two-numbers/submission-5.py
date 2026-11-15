# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr = node = ListNode()
        storeVal = 0
        while l1 and l2:
            val = l1.val + l2.val + storeVal
            if val >= 10:
                node.val = val % 10
                storeVal = 1
            else:
                node.val = val
                storeVal = 0
            l1 = l1.next
            l2 = l2.next
            if l1 and l2:
                node.next = ListNode()
            else:
                if storeVal > 0 or l1 or l2:
                    node.next = ListNode()
                else:
                    node.next = None
            node = node.next
        if l1 or l2:
            while l1:
                val = l1.val + storeVal
                if val >= 10:
                    node.val = val % 10
                    storeVal = 1
                else:
                    node.val = val
                    storeVal = 0
                l1 = l1.next
                if storeVal == 0:
                    node.next = l1
                    return ptr
                else:
                    if l1:
                        node.next = ListNode()
                    else:
                        node.next = ListNode(storeVal)
                        node = node.next
                        node.next = None
                node = node.next
            while l2:
                val = l2.val + storeVal
                if val >= 10:
                    node.val = val % 10
                    storeVal = 1
                else:
                    node.val = val
                    storeVal = 0
                l2 = l2.next
                if storeVal == 0:
                    node.next = l2
                    return ptr
                else:
                    if l2:
                        node.next = ListNode()
                    else:
                        node.next = ListNode(storeVal)
                        node = node.next
                        node.next = None
                node = node.next
        elif storeVal > 0:
            print("we hit this")
            node.val = storeVal
            node.next = None
        return ptr            
