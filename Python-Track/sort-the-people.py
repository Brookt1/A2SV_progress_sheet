class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(len(heights)-1,-1,-1):

            min_idx=i
            for j in range(0,i):
                if heights[j]<heights[min_idx]:
                    min_idx=j
            names[i],names[min_idx]=names[min_idx],names[i]
            heights[i],heights[min_idx]=heights[min_idx],heights[i]
        return names

        