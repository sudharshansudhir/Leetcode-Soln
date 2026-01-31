class Solution:
    def toGoatLatin(self, sentance: str) -> str:
        sentance=sentance.split()
        ans=[]
        for i in range(len(sentance)):
            t=sentance[i]
            if(sentance[i][0].lower() in "aeiou"):
                t+="ma"
            else:
                t=t[1:]+t[0]+"ma"
            for k in range(i+1):
                t+="a"
            ans.append(t)
        d=""
        for i in ans:
            d+=i
            d+=" "
        return d.strip()
