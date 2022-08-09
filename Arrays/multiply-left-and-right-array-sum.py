def multiply (arr, n) : 
    l=arr[:n//2]
    r=arr[n//2:]
    s=sum(l)*sum(r)
    return s