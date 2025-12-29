class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans=[]
        one="qwertyuiop"
        two="asdfghjkl"
        thr="zxcvbnm"
        for i in words:
            a=i
            c1=c2=c3=0
            for j in a:
                if(j.lower() in one):
                    c1+=1
                elif(j.lower() in two):
                    c2+=1
                elif(j.lower() in thr):
                    c3+=1
            print(c1,c2,c3,a)
            if(c1==len(a) or c2==len(a) or c3==len(a)):
                ans.append(a)
        return ans

