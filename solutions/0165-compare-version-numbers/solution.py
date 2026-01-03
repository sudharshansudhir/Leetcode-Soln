class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split(".")
        v2=version2.split(".")
        if(len(v1)<len(v2)):
            for i in range(abs(len(v1)-len(v2))):
                v1.append("0")
        elif(len(v1)>len(v2)):
            for i in range(abs(len(v1)-len(v2))):
                v2.append("0")
        a=list(map(int,v1))
        b=list(map(int,v2))
        for i in range(len(a)):
            if(a[i]<b[i]):
                return -1
            elif(a[i]>b[i]):
                return 1
        return 0
