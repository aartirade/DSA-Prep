class Solution:
    def MaxNumber(self, arr, n):
        arr.sort(reverse=True)
        a="".join(map(str,arr))
        return a


#Input:
#N = 5
#A[] = {9, 0, 1, 3, 0}
#Output:
#93100