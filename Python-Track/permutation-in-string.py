class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        dic=Counter(s1)
        left=0
        sub_dic=defaultdict(int)
        for right in range(len(s2)):
            sub_dic[s2[right]]+=1
            if right-left+1==len(s1):
                if sub_dic==dic:
                    return True
                sub_dic[s2[left]]-=1
                if sub_dic[s2[left]]<1:
                    del sub_dic[s2[left]]
                left+=1
        return False




        