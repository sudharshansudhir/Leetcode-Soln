class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        s=[]
        i=0
        while gifts and i<k:
            maxi=max(gifts)
            ind=gifts.index(maxi)
            gifts.pop(ind)
            sq=int(maxi**0.5)
            gifts.insert(ind,sq)
            s.append(sq)
            i+=1
        print(s)
        return sum(gifts)
