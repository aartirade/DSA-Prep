def intersetPoint(head1,head2):
    d={}
    p1=head1
    p2=head2
    
    while p1:
        if p1 not in d:
            d[p1]=1
        p1=p1.next
        
    while p2:
        if p2 in d:
            return p2.data
        p2=p2.next
        