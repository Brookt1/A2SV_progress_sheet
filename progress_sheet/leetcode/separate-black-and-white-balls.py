class Solution:
    def minimumSteps(self, s: str) -> int:
        

        holder=seeker=0
        line=[*s]
        res=0
        while seeker<len(s):
            if line[seeker]=='0' and line[holder]=='1':
                line[seeker],line[holder]=line[holder],line[seeker]
                res+=seeker-holder
                seeker+=1
                holder+=1
            elif line[holder]=='0' and holder<seeker:
                holder+=1
            else:
                seeker+=1
        return res
            
