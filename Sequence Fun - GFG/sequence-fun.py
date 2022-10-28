#User function Template for python3

class Solution:
	def NthTerm(self, n):
	    s=1
	    mod=10**9+7
	    for i in range(1,n+1):
	        s=(s*i+1)%mod
	    return s
		# Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.NthTerm(n)
		print(ans)

# } Driver Code Ends