def printNumber(s,n):
    k=[]
    for i in s:
        if i in "abc":
            k.append("2")
        if i in "def":
            k.append("3")
        if i in "ghi":
            k.append("4")
        if i in "jkl":
            k.append("5")
        if i in "mno":
            k.append("6")
        if i in "pqrs":
            k.append("7")
        if i in "tuv":
            k.append("8")
        if i in "wxyz":
            k.append("9")
    return "".join(k)
            