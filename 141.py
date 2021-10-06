# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        # U: [3,2,0,4]
        # U: [0,1,0]
        # U: []
        # U: [1]
        
        if not head:
            return False
        
        dum1 = dum2 = ListNode()
        
        dum1.next = head
        dum2.next = head.next
        
        while dum2 and dum2.next:
            dum1 = dum1.next
            dum2 = dum2.next.next
            if dum1 == dum2:
                return True
        return False
    
        
        # head.next = 3
        
#         dum1.next = head
#         dum2.next = 1
#         dum1 = head
#         dum2 = 1