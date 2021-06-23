# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        LL = None # node to the left of left
        RR = None # node to the right of right
        
        node = head
        nL = []
        
        i = 1
        if left==1:
            nL.append(node)
        elif left==2:
            LL = node
        
        while i < right+1 and node.next:
            node = node.next
            i += 1
            
            if left <= i <= right:
                nL.append(node)
            elif i==right + 1:
                RR = node
            elif i==left - 1:
                LL = node
        
        # list of nodes should be complete now
        #print(nL)
        
        node = nL.pop()
        if LL:
            LL.next = node
        else:
            head = node
        
        while nL != []:
            node.next = nL.pop()
            node = node.next
        
        if RR:
            node.next = RR
        else:
            node.next = None
        
        return head
            
