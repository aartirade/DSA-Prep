class Solution:
    def rearrange(self,arr, n):
        pos=[]
        neg=[]
        for i in range(n):
            if arr[i]>=0:
                pos.append(arr[i])
            else:
                neg.append(arr[i])
                
        arr[:]=pos[:]
        idx=1
        for j in neg:
            arr.insert(idx,j)
            idx+=2 
        return arr