class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans=[]
        for i in range(len(l)):
            arr=nums[l[i]:r[i]+1]
            a=True
            if(len(arr)<2):
                a=False
            else:
                arr.sort()
                print(arr)
                for j in range(0,len(arr)-1):
                    if not(abs(arr[j]-arr[j+1])==abs(arr[1]-arr[0])):
                        # print(arr[j],arr[j+1])
                        a=False
            
            ans.append(a)
        return ans

                

