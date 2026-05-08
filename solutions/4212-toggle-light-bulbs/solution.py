class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        a=[]
        for i in bulbs:
            if i not in a:
                a.append(i)
            else:
                a.remove(i)
        a.sort()
        return a
