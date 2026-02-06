class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s=s.split()
        no=[]
        for i in s:
            if i.isdigit():
                no.append(int(i))
        # flag=True
        print(no)
        for i in range(len(no)-1):
            if no[i]>=no[i+1]:
                return False
        return True
