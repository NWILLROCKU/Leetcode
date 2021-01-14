# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(2)
l1_head = l1
l1.next = ListNode(4)
l1_nonhead = l1.next
l1_nonhead.next = ListNode(3)

l2 = ListNode(5)
l2_head = l2
l2.next = ListNode(6)
l2_nonhead = l2.next
l2_nonhead.next = ListNode(4)

print('starting l1 =' + str(l1.val))
print('starting l2 =' + str(l2.val))

nodeSum = l1.val + l2.val
if nodeSum < 10:
    lsum = ListNode(nodeSum)
    extra_one = 0
else:
    lsum = ListNode(nodeSum-10)
    extra_one = 1
    
lsum_head = lsum
while l1.next != None or l2.next != None or extra_one == 1:
    print('hi')
    if l1.next != None:
        l1 = l1.next
        print('went to next l1')
        if l2.next != None:
            l2 = l2.next
            print('went to next l2')
            nodeSum = l1.val + l2.val + extra_one
            print('added l1 and l2')
        else:
            nodeSum = l1.val + extra_one
            print('added l1 only')
    elif l2.next != None:
        l2 = l2.next
        print('went to next l2')
        nodeSum = l2.val + extra_one
        print('added l2 only')
    else:
        print('adding extra 1')
        nodeSum = extra_one
        
    if nodeSum < 10:
        lsum.next = ListNode(nodeSum)
        extra_one = 0
    else:
        lsum.next = ListNode(nodeSum-10)
        extra_one = 1
    lsum = lsum.next
    print('added to lsum')
