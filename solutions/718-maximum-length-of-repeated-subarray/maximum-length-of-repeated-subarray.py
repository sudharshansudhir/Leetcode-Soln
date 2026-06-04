class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp=[[-1]*(len(nums2)+1) for km in range(len(nums1)+1)]
        n1=len(nums1)
        n2=len(nums2)
        for i in range(n1+1):
            dp[i][0]=0
        ans=0
        for i in range(n2+1):
            # print(dp[0])
            dp[0][i]=0
        # print(dp)

        # print(dp)
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if not nums1[i-1]==nums2[j-1]:
                    dp[i][j]=0
                    # max(dp[i-1][j],dp[i][j-1])
                else:
                    dp[i][j]=1+dp[i-1][j-1]
                    ans=max(ans,dp[i][j])
        # print(dp)
        # m=0
        # for i in dp:
        #     m=max(m,max(i))
        return ans
