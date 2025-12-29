class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        m=0
        for i in arr1:
            c=0
            f=0
            for j in arr2:
                if(abs(i-j)>d):
                    c+=1
                # else:
                #     f+=1

            if(c==len(arr2)):
                m+=1
        return m


