class Solution:
    def smallestNumber(self, num: int) -> int:
        if len(str(num))<2: return num
        if num>=0:
            val=[*str(num)]
            val.sort()
            i=0
            while val[i]=='0':
                i+=1
            for j in range(i): val.insert(i+1,'0')
            return int(''.join(val))
        else:
            val=[*str(num)[1:]]
            val.sort()
            val.reverse()
            if val[0]=='0':
                val[0],val[1]=val[1],val[0]
            return -1*int(''.join(val))

        