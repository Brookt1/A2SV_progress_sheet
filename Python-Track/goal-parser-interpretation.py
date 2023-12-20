class Solution:
    def interpret(self, comm: str) -> str:

        res=''

        i=0
        while i<len(comm):

            if comm[i]=='G': 
                res+='G'
                i+=1
            elif comm[i+1]==')': 
                i+=2
                res+='o'
            else:
                i+=4
                res+='al'
        return res
        