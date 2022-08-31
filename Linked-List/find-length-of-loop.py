def countNodesinLoop(head):
    s=head
    f=head
    while f and f.next:
        s=s.next
        f=f.next.next
        
        if s==f:
            c=1
            s=s.next
            while s!=f:
                c+=1
                s=s.next
            return c
    return 0