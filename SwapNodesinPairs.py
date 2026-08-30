# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr=head
        if curr:
            second=curr.next
        if curr==None:
            return None
        if curr.next == None:
            return curr
        result=self.swapPairs(curr.next.next)
        curr.next.next=curr
        curr.next=result
        return second
