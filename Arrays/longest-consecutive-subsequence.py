class Solution:
    def findLongestConseqSubseq(self,arr, N):
        arr=set(arr)
        arr=list(arr)
        arr.sort()
        if len(arr)==1:
            return 1
        t=1
        ans=0
        for i in range(len(arr)-1):
            if arr[i]+1==arr[i+1]:
                t+=1
            else:
                t=1
            ans=max(ans,t)
        return ans
        