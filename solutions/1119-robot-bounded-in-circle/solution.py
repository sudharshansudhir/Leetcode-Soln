class Solution:
    def isRobotBounded(self, inst: str) -> bool:
        curr=[0,0]
        north=True
        south=False
        east=False
        west=False
        for j in range(4):
            for i in inst:
                if i=="G":
                    if north:
                        curr[1]+=1
                    elif south:
                        curr[1]-=1
                    elif east:
                        curr[0]+=1
                    else:
                        curr[0]-=1
                elif i=="L":
                    if north:
                        north=False
                        west=True
                    elif west:
                        west=False
                        south=True
                    elif south:
                        south=False
                        east=True
                    elif east:
                        east=False
                        north=True
                else:
                    if north:
                        north=False
                        east=True
                    elif east:
                        east=False
                        south=True
                    elif south:
                        south=False
                        west=True
                    elif west:
                        west=False
                        north=True
            if curr==[0,0]:
                return True
        return False

