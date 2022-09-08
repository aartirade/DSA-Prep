class Solution:
    def solve(self, arr, n):
        arr.sort()
        o=""
        e=""
        if n<=1:
            return arr[0]
        for i in range(0,n,2):
            e+=str(arr[i])
        for i in range(1,n,2):
            o+=str(arr[i])
        res=int(e)+int(o)
        return str(res)