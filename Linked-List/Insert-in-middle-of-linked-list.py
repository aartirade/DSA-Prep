def insertInMid(head,node):
    slow=head
    fast=head
    curr=head
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
    node.next=slow.next
    slow.next=node
