class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''

def findIntersection(head1,head2):

    ll= linkedList()
    h1=head1
    h2=head2
    while h1 and h2:
        if h1.data==h2.data:
            ll.insert(h1.data)
            h1=h1.next
            h2=h2.next
            
        elif h2.data>h1.data:
            h1=h1.next
        else:
            h2=h2.next
            
    return ll.head