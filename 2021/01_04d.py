        class ListNode(object):
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
                
        # Initialize l3 / return l3 if either l1 or l2 is []
        if l1==None:
            return l2
        else:
            if l2==None:
                return l1
            else:
                if l1.val > l2.val:
                    l3 = ListNode(l2.val)
                    l2 = l2.next
                else:
                    l3 = ListNode(l1.val)
                    l1 = l1.next
                l3_head = l3
                
        while l1 != None or l2 != None: # Haven't finished going through l1 and/or l2
            if l1==None:
                l3.next = l2
                return l3_head
            else:
                if l2==None:
                    l3.next = l1
                    return l3_head
                else:
                    if l1.val > l2.val:
                        l3.next = l2
                        l3 = l3.next
                        l2 = l2.next
                    else:
                        l3.next = l1
                        l3 = l3.next
                        l1 = l1.next
        return l3_head
