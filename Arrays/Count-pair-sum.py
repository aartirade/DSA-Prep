class Solution:
    def countPairs(self,arr1, arr2, M, N, x):
        p=0
        l=0
        r=N-1
        
        while l<M and r>=0:
            if arr1[l]+arr2[r]==x:
                l+=1
                r-=1
                p+=1
                
            elif arr1[l]+arr2[r] < x:
                l+=1
                
            else:
                r-=1
                
        return p