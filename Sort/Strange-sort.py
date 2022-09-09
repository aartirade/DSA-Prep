class Solution:
    def strangeSort (self,arr, n, k):
        K=arr[k-1]
        arr.sort()
        arr.remove(K)
        arr.insert(k-1,K)
        return arr