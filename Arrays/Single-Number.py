class Solution:
    
    def getSingle(self,arr, n):
        d={}
        num=0
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
                
        for i in d:
            if d[i]%2!=0:
                num=i
        return num