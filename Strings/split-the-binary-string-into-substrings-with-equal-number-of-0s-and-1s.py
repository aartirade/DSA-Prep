class Solution:
    def maxSubStr(self,str):
        c0=0
        c1=0
        c=0
        for i in range(len(str)):
            if str[i]=="0":
                c0+=1
            else:
                c1+=1
            
            if c0==c1:
                c+=1
            
        if c0!=c1:
            return -1
        return c