class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        
        if root ==None:
            return 0
            
        l=self.height(root.left)
        r=self.height(root.right)
        if l<r:
            return r+1
        else:
            return l+1