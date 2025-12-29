class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maxi=0
        for i in strs:
            if not i.isdigit():
                if(len(i)>maxi):
                    maxi=len(i)
            else:
                if(int(i)>maxi):
                    maxi=int(i)
        return maxi
