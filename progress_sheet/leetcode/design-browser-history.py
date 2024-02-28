class ListNode:
    def __init__(self,url='',next=None,prev=None):
        self.url=url
        self.next=next
        self.prev=prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = ListNode(homepage)
        
    def visit(self, url: str) -> None:
        
        self.current.next=ListNode(url,None,self.current)
        self.current=self.current.next

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.current.prev:
                self.current=self.current.prev
        return self.current.url

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.current.next:
                self.current=self.current.next
        return self.current.url
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)