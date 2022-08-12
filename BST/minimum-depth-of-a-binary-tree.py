class Solution:
    def minDepth(self, root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        l=self.minDepth(root.left)
        r=self.minDepth(root.right)
            
        if l==0 or r==0:
            return max(l,r)+1
        else:
            return min(l,r)+1