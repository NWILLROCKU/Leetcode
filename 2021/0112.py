# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next = ListNode(4)

nodeSum = l1.val + l2.val
if nodeSum < 10:
    lsum = ListNode(nodeSum)
    extra_one = 0
else:
    lsum = ListNode(nodeSum-10)
    extra_one = 1
lsum_head = lsum
while l1.next != None or l2.next != None or extra_one == 1:
    if l1.next != None:
        l1 = l1.next
        if l2.next != None:
            l2 = l2.next
            nodeSum = l1.val + l2.val + extra_one
        else:
            nodeSum = l1.val + extra_one
    elif l2.next != None:
        l2 = l2.next
        nodeSum = l2.val + extra_one
    else:
        nodeSum = extra_one
        
    if nodeSum < 10:
        lsum.next = ListNode(nodeSum)
        extra_one = 0
    else:
        lsum.next = ListNode(nodeSum-10)
        extra_one = 1
