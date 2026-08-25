# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr=head
        new_head=None
        if head == None:
            return None
        if curr.next==None:
            return curr
        new_head=self.reverseList(curr.next)
        curr.next.next=curr
        curr.next=None
        return new_head
        
        
            

       
    
        
