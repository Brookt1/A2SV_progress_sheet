class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            pt=len(st)-1
            if pt==-1 or i=='{' or i=='[' or i=='(':
                st.append(i)
            else:
                if i=='}' and st[pt]=='{':
                    st.pop()
                elif i==']' and st[pt]=='[':
                    st.pop()
                elif i==')' and st[pt]=='(':
                    st.pop()
                else:
                    return False
        
        if not st:
            return True
        return False