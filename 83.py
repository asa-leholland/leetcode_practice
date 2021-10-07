# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
  
# U: [1,1,2,3,3]
# U: [1,1,1,2,3,3,3]
# U: []
# U: [1]

# need a dummy head
# need two pointers (node, and node.next)
        
        if not head:
            return head
        
        
        current = head
        
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head
    
    
#     test 1: [1,1,2,3,3]
#       current.next is not None
# current.val = 1 which equlas current.next.val
#     [1] -> [1] => [1->2]