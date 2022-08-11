class Solution:
    # Return the Kth smallest element in the given BST 
    def KthSmallestElement(self, root, K): 
        l=[]
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            l.append(root.data)
            inorder(root.right)
           
        inorder(root)
       
        if len(l)==0 or len(l)<=K-1:
            return -1
        else:
            return l[K-1]
       