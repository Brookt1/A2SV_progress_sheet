class MyCircularQueue:

    def __init__(self, k: int):
        self.array=[0]*k
        self.front=-1
        self.rear=-1
    def enQueue(self, value: int) -> bool:
        n=len(self.array)

        # checking if our queue is empty. if it is empty return False
        if (self.rear+1)%n==self.front:
            return False
        
        # setting the front to index 0 if our array is empty
        if self.front==-1:
            self.front=0
        # getting rear position and setting value
        self.rear=(self.rear+1)%n
        self.array[self.rear]=value

        return True

    def deQueue(self) -> bool:

        if self.front==-1:
            return False

        if self.rear == self.front:
            self.rear = self.front = -1
        else:
            self.front=(self.front+1)%len(self.array)
        
        return True

    def Front(self) -> int:

        if self.front==-1:
            return -1
        return self.array[self.front]

    def Rear(self) -> int:
        if self.rear==-1:
            return -1
        return self.array[self.rear]
        
    def isEmpty(self) -> bool:

        return self.front == -1
        

    def isFull(self) -> bool:

        return (self.rear+1)%len(self.array)==self.front
        
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()