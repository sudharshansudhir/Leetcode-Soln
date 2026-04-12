class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        c=0
        for i in range(1,len(arr)+1,2):
            # k=i-1
            j=0
            while j+i<=len(arr):
                subarr=arr[j:j+i]
                print(subarr)
                j+=1
                c+=sum(subarr)
        # print(c)
        return c

