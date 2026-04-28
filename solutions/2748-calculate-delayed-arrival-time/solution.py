class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        s=arrivalTime+delayedTime
        if s>=24:
            return s%24
        return s
