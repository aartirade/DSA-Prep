class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        a=""
        b=""
        while first:
            a=a+str(first.data)
            first=first.next
        while second:
            b=b+str(second.data)
            second=second.next
            
        s=int(a)+int(b)
        s=str(s)
        s=" ".join(s)
        return Node(s)
        