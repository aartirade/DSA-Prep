class Solution:
    def getCount(self, head_node):
        curr=head_node
        c=1
        while curr.next:
            c=c+1
            curr=curr.next
        return c
            