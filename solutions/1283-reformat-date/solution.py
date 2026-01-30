class Solution:
    def reformatDate(self, date: str) -> str:
        dict={
            "Jan":"01",
            "Feb":"02",
            "Mar":"03", 
            "Apr":"04", 
            "May":"05" ,
            "Jun":"06", 
            "Jul":"07",
            "Aug":"08", 
            "Sep":"09", 
            "Oct":"10", 
            "Nov":"11", 
            "Dec":"12"
        }
        date=date.split()
        date=date[::-1]
        ans=date[0]
        ans+="-"
        ans+=dict[date[1]]
        ans+="-"
        t=date[2][:len(date[2])-2]
        print(t)
        if(len(t)<2):
            d="0"+t
        else:
            d=t
        ans+=d
        return ans
