class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        i=0
        j=0
        c=0
        players.sort()
        trainers.sort()
        while players and j<len(trainers):
            if players[i]<=trainers[j]:
                c+=1
                players.remove(players[i])
                trainers.remove(trainers[j])
                j=0
            else:
                j+=1
        return c
