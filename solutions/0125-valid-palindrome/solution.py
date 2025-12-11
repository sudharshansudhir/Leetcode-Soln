class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        for i in s:
            if 65<=ord(i)<91 or 97<=ord(i)<123 or i in "1234567890":
                if(i in "1234567890"):
                    ans+=i
                else:
                    ans+=i.lower()
        print(ans,ans[::-1])
        return ans==ans[::-1]
