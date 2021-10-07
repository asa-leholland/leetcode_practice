# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# U

# a1-> a2-> c1 -> c2 -> c3
# b1 -> b2 -^
# return c1

# a1-> a2-> c1 
# b1 -^
# return a2

#a1
#b1
# return null

# a1 -> b2
# c1   -^
# return null

# dummyhead
# two pointer
# reverse
# multi-pass

# multipass approach
# since the two lists can only be identical if they are the same length, first step is to trim the lists
# iterate over each list to obtain the length.
# determine which list is longer, and obtain the difference between the two
# then, trim the longer list so that the two lists are the same length
# then iterate over both lists, comparing if the nodes are equal. If so, return.
# if you reach the end of the nodes without a match, return null
# 3, #2
def get_intersection(head1, head2):

  len1 = len2 = 0
  cur1 = head1
  cur2 = head2

  while cur1.next:
    len1 += 1
    cur1 = cur1.next
  
  while cur2.next:
    len2 += 1
    cur2 = cur2.next
  

  # len1 =1 len2 = 2
  cur1 = head1
  cur2 = head2

  i = 0
  if len1 > len2:
    while i < (len1 - len2):
      cur1 = cur1.next
      i += 1
  elif len2 > len1:
    while i < (len2 - len1):
      cur2 = cur2.next
      i += 1
  
  while cur2 and cur1:
    if cur2 == cur1:
      return cur2
    else:
      cur2 = cur2.next
      cur1 = cur1.next
    
  return None
  


#     3
# 2   -^
# return null


  
# a1-> a2-> c1 
# b1 -^
# return a2
