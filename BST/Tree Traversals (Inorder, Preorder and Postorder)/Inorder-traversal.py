class Solution:
    def InOrder(self,root):
        l=[]
        if root ==None:
            return l
        
        l.extend(self.InOrder(root.left))
        l.append(root.data)
        l.extend(self.InOrder(root.right))
        
        return l