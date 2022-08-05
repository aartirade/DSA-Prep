def getNthFromLast(head,n):
    curr=head
    l=[]
    while head:
        l.append(head.data)
        head=head.next
    if n>len(l):
        return -1
    return l[-n]