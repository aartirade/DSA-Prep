class Solution:
    def kthLargest(self,root, k):
        l=[]
        if root==None:
            return 0
        if root.left ==None and root.right==None:
            return 1
        if not root:
            return 0
            
        def traverse(node):
            if node:
                l.append(node.data)
                traverse(node.left)
                traverse(node.right)
        traverse(root)
        l.sort(reverse=True)
        return l[k-1]