# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k==1:
            return head
        
        node = head
        myList = [head]
        lastNode = -1
        while node.next != None:
            node = node.next
            if len(myList)==k:
                myList.reverse()
                if lastNode==-1:
                    head = myList[0]
                else:
                    lastNode.next = myList[0]

                for i in range(1, k):
                    myList[i-1].next = myList[i]
                lastNode = myList[-1]
                myList = []
            #print(node.val)
            myList.append(node)
        
        if len(myList)==k:
            myList.reverse()
            
        if lastNode==-1:
            head = myList[0]
        else:
            lastNode.next = myList[0]
            
        for i in range(1, len(myList)):
            myList[i-1].next = myList[i]
        myList[-1].next = None
            
        return head
