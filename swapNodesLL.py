# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        nL = [head]
        node = head
        while node.next != None:
            node = node.next
            nL.append(node)
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
