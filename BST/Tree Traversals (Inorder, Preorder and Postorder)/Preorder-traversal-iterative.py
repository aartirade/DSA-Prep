
class Solution:
   
    def preOrder(self, root):
        s=[root]
        res=[]
        if root==None:
            return root
        
        while len(s)>0:
            node=s.pop()
            res.append(node.data)
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
        return res