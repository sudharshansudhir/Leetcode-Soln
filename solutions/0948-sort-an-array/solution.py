class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr):
            if(len(arr)<=1):
                return arr
            mid=len(arr)//2
            left=arr[:mid]
            right=arr[mid:]
            sright=merge(right)
            sleft=merge(left)

            return sortt(sright,sleft)
        
        def sortt(right,left):
            i=0
            j=0
            c=[]
            while i<len(right) and j<len(left):
                if right[i]<left[j]:
                    c.append(right[i])
                    i+=1
                else:
                    c.append(left[j])
                    j+=1
            if j<len(left):
                for s in range(j,len(left)):
                    c.append(left[s])
            else:
                for s in range(i,len(right)):
                    c.append(right[s])
            return c
        sortedlist=merge(nums)
        return sortedlist
                

