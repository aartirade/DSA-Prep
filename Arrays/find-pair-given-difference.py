class Solution:

    def findPair(self, arr, L,N):
        arr.sort()
        i,j=0,1
        while i<L and j<L:
            if i!=j and arr[j]-arr[i]==N:
                return True
            elif arr[j]-arr[i]<N:
                j+=1
            else:
                i+=1
        return False
       