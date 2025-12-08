class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=""
        for i in digits:
            a+=str(i)
        a=int(a)
        a=a+1
        a=str(a)
        lst=[]
        for i in a:
            lst.append(int(i))
        return lst
