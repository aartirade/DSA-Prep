class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        
        if root==None:
            return None
            
        if root.left:
            self.mirror(root.left)
        if root.right:
            self.mirror(root.right)
        root.left,root.right=root.right,root.left