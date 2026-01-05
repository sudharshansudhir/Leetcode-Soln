class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ans=[]
        sentence=sentence.split()
        dictionary.sort(key=len)
        for i in sentence:
            flag=True
            for j in dictionary:
                if j == i[0:len(j)]:
                    ans.append(j)
                    flag=False
                    break
            if(flag):
                ans.append(i)
        an=""
        print(ans)
        for i in ans:
            an+=i
            an+=" "
        return an.strip()
                

