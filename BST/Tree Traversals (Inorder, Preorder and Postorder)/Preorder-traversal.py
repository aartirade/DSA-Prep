def preorder(root):
    l=[]
    
    if root==None:
        return l
    
    l.append(root.data)
    l.extend(preorder(root.left))
    l.extend(preorder(root.right))
    
    return l