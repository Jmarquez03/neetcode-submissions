"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = defaultdict(lambda: Node(0))
        copies[None] = None
        ptr = head
        while head:
            copies[head].val = head.val
            copies[head].next = copies[head.next]
            copies[head].random = copies[head.random]
            head = head.next
        return copies[ptr]