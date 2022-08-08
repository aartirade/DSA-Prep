def countRev (s):
    o=0
    c=0

    if len(s)%2!=0:
        return -1
        
    for i in range(len(s)):
        if s[i]=="{":
            o+=1
        else:
            o-=1
            
            if o<0:
                c+=1
                o=1
    return c+o//2