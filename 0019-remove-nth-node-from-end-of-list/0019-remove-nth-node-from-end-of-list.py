# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recursiveHelper(self, head: Optional[ListNode], n: int) -> (Optional[ListNode], int):
        if (head == None):
            return (None, 0)
        else:
            (chain, location) = self.recursiveHelper(head.next, n)
            location += 1
            if (location == n):
                return (chain, location)
            else:
                return (ListNode(head.val, chain), location)

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        (head, location) = self.recursiveHelper(head, n)
        return head