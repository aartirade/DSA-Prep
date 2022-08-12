class Solution:

    def sameChar(self, A, B):
        A=A.lower()
        B=B.lower()
        c=0
        for i in range(len(A)):
            if A[i]==B[i]:
                c+=1
        return c