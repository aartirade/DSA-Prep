class Solution:
    def MedianOfArrays(self, array1, array2):
        a3=array1+array2
        a3.sort()
        n=len(a3)
        h=n//2
        if n%2!=0:
            return a3[n//2]
        m=a3[n//2]+a3[n//2-1]
        if m%2==0:
            return m//2
        return m/2