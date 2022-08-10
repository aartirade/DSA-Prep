def insert(root, Key):
    if root==None:
        return Node(Key)
    else:
        if root.data==Key:
            return root
        elif root.data<Key:
            root.right=insert(root.right,Key)
        else:
            root.left=insert(root.left, Key)
    return root