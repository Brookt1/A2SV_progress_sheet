class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        order_dic={x:i for i,x in enumerate(order)}
        for i in range(len(words)-1):
            leng1=len(words[i])
            leng2=len(words[i+1])
            j=0
            while j<min(leng1,leng2):
                if order_dic[words[i][j]]>order_dic[words[i+1][j]]: 
                    return False
                if order_dic[words[i][j]]<order_dic[words[i+1][j]]: 
                    break
                j+=1
            if leng1>leng2 and words[i+1] in words[i]: 
                return False
        return True