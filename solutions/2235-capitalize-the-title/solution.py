class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title=title.split()
        ans=""
        for i in title:
            if len(i)<=2:
                ans+=i.lower()
            else:
                ans+=i.capitalize()
            ans+=" "
        return ans.strip()
