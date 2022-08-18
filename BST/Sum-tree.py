class Solution:
    def isSumTree(self,root):
        if root==None:
            return 0
        
        if root.left==None and root.right==None:
            return root.data

        l=self.isSumTree(root.left)
        r=self.isSumTree(root.right)
        
        summ=l+r
        if summ!=root.data:
            return 0
        # return l+r
        return root.data+ l+r