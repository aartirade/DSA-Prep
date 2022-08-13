class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        curr=head
        while curr.next!=None:
            curr=curr.next
        curr.next=head
        
        i=0
        while i<k:
            curr=curr.next
            i+=1
        head=curr.next
        curr.next=None
        return head