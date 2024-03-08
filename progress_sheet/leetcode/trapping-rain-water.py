class Solution:
    def trap(self, height: List[int]) -> int:
        st=[]
        res=0
        for i in range(len(height)):

            while st and  st[0]<=height[i] :
                val=st[0]-st.pop()
                res+=val if val>0 else 0
            st.append(height[i])
        h=st[::-1]
        st=[]
        for i in range(len(h)):
            while st and  st[0]<=h[i] :
                val=st[0]-st.pop()
                res+=val if val>0 else 0
            st.append(h[i])

        return res






            
        