class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root ):
        
        res=[]
        q=[]
        q.append(root)
        if root==None:
            return None
            
        while len(q)!=0:
            root=q.pop(0)
            res.append(root.data)
            if root.left!=None:
                q.append(root.left)
            if root.right!=None:
                q.append(root.right)
        return res