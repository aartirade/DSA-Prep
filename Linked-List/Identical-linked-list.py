def areIdentical(head1, head2):
    if head1==None and head2==None:
        return True
    
    while head1!=None and head2!=None:
        if head1.data!=head2.data:
            return False
        head1=head1.next
        head2=head2.next
    return True
  