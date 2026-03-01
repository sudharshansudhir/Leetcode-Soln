class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref)==1:
            return pref
        arr=[pref[0]]
        for i in range(len(pref)-1):
            arr.append(pref[i]^pref[i+1])
        return arr
