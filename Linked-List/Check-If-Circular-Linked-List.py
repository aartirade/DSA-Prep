def isCircular(head):
    curr=head
    while curr:
        curr=curr.next
        if curr==head:
            return 1
    return 0