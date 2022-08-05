class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        
        curr=head
        s=set()
        while curr:
            if curr.next in s:
                curr.next=None
            s.add(curr)   
            curr=curr.next