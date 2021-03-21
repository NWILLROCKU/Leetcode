# Definition for singly-linked list.
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
        nL = [head]
        node = head
        while node.next != None:
            node = node.next
            nL.append(node)
            
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
