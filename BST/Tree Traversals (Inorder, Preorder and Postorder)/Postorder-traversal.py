def postOrder(root):
    l=[]
    if root==None:
        return l
    
    l.extend(postOrder(root.left))
    l.extend(postOrder(root.right))
    l.append(root.data)
    
    return l