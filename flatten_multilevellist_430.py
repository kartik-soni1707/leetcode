"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        last=[None]
        def explore(node):
            if not node:
                return None
            prev=last[0]
            node.prev=prev
            if prev:
                prev.next=node
            last[0]=node
            saved=node.next
            if node.child:
                temp=node.child
                node.child=None
                explore(temp)
            explore(saved)
        explore(head)
        return head