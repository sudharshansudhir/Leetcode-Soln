class Solution:
    def slowestKey(self, rls: List[int], keys: str) -> str:
        key=[]
        m=0
        last=-1
        for i in range(len(rls)):
            if i==0:
                m=rls[i]
                key=[keys[i]]
                last=rls[i]
            else:
                if rls[i]-last>m:
                    m=rls[i]-last
                    key=[keys[i]]
                if rls[i]-last==m:
                    m=rls[i]-last
                    key.append(keys[i])
                last=rls[i]
        key.sort(reverse=True)
        return key[0]