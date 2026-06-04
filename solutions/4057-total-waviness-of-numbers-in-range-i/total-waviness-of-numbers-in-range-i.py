class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans=0
        for i in range(num1,num2+1):
            i=str(i)
            n=len(i)
            if not n<=2:
                j=1
                while j+1<n:
                    if (i[j]>i[j-1] and i[j]>i[j+1]) or (i[j]<i[j-1] and i[j]<i[j+1]):
                        ans+=1
                    j+=1
            # if not n<=2:
            #     if n%2==1:
            #         mid=n//2
            #         if int(i[mid-1])< int(i[mid]) and int(i[mid])>int(i[mid+1]):
            #             ans+=1
            #         elif int(i[mid-1])> int(i[mid]) and int(i[mid])<int(i[mid+1]):
            #             ans+=1
            #     else:
            #         mid=(n//2)-1
            #         if int(i[mid-1])< int(i[mid]) and int(i[mid])>int(i[mid+1]):
            #             ans+=1
            #         elif int(i[mid-1])> int(i[mid]) and int(i[mid])<int(i[mid+1]):
            #             ans+=1
                    
            #         mid=n//2
            #         if int(i[mid-1])< int(i[mid]) and int(i[mid])>int(i[mid+1]):
            #             ans+=1
            #         elif int(i[mid-1])> int(i[mid]) and int(i[mid])<int(i[mid+1]):
            #             ans+=1
        return ans
