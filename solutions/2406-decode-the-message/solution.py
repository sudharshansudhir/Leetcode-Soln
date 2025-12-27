class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        a=""  
        for i in key:
            if i.isalpha() and i not in a:
                a+=i
        ans=""
        for i in range(len(message)):
            if(message[i].isalpha()):
                ind=a.index(message[i])
                print(ind)
                ans+=chr(ind+97)
            else:
                ans+=" "
        return ans

      
