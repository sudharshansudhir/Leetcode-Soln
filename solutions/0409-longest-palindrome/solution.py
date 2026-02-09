class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans=[]
        # s=s.lower()
        l=[]
        # f=False
        if s==s[::-1]:
            return len(s)
        nl=[]
        for i in s:
            if s.count(i)>=2 and i not in l:
                if s.count(i)%2==0:
                    ans.append(s.count(i))
                else:
                    ans.append(s.count(i)-1)
                l.append(i)
                # f=True
        
            # else:
                # if i not in nl and i not in l:
                #     nl.append(i)
        if sum(ans)%2==1 or sum(ans)==len(s):
            return sum(ans)
        return sum(ans)+1
