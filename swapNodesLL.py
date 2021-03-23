# Definition for singly-linked list.
<<<<<<< HEAD
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
=======
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Get nL
>>>>>>> cc5577fa396f9a842382f04c02277a83d8e9072b
        nL = [head]
        node = head
        while node.next != None:
            node = node.next
            nL.append(node)
<<<<<<< HEAD
        if k-1 == len(nL)-k:
            return head
        
        # Swap nodes in nL
        node1 = nL[k-1]
        node2 = nL[-k]
        nL[-k] = node1
        nL[k-1] = node2

        if k > 1:
            nL[k-2].next = nL[k-1]
            nl[-k].next = nL[-k + 1]
        else:
            nL[-k].next = None

        return nL[0]
=======
            
        # Swap nodes
        node1 = nL[k-1]
        node2 = nL[-k]
        nL[k-1] = node2
        nL[-k] = node1
        
        if k > 1:
            nL[k-2].next = nL[k-1]
            nL[-k].next = nL[-k+1]
        else:
            nL[-k].next = None
        if k < len(nL):
            nL[k-1].next = nL[k]
            nL[-k-1].next = nL[-k]
        else:
            nL[k-1].next = None
        
        return nL[0] # return head
>>>>>>> cc5577fa396f9a842382f04c02277a83d8e9072b
