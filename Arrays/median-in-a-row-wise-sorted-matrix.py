import statistics as st
class Solution:
    def median(self, matrix, r, c):
        m=[]
        for i in range(r):
            for j in range(c):
                m.append(matrix[i][j])
        
        m.sort()
        return st.median(m)
