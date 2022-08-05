class LinkedList:
    def __init__(self):
        self.head = None
This is method only submission.
 You only need to complete below method.
"""
def getNth(head, k):

    l=[]
    while head:
        l.append(head.data)
        head=head.next
    
    return l[k-1]
