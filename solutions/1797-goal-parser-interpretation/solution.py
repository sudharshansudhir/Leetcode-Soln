class Solution:
    def interpret(self, command: str) -> str:
        ans=""
        for i in range(len(command)-1):
            if command[i]=="(" and command[i+1]==")":
                ans+="o"
            else:
                if command[i].isalpha():
                    ans+=command[i]
        if(command[-1].isalpha()):
            ans+=command[-1]
        return ans
            
