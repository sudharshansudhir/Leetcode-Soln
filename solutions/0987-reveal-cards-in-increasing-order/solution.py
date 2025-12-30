class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # if(len(deck)<=2):
        #     return deck       
        d=[]
        deck.sort(reverse=True)
        for i in range(0,len(deck)):
            if(len(d)<2):
                d.insert(0,deck[i])
            else:
                a=d.pop()
                d.insert(0,a)
                d.insert(0,deck[i])
        print(d)
        return d
        
