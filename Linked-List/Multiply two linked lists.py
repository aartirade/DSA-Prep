class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def multiplyTwoList(head1, head2):
    l1=''
    l2=''
    while head1:
        l1+=str(head1.data)
        head1=head1.next
    
    while head2:
        l2+=str(head2.data)
        head2=head2.next
        
    ans=int(l1)*int(l2)
    return ans%1000000007