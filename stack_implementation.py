class Stack:
    def __init__(self):
        self.list=[]
    def is_empty(self):
        return len (self.list)==0
           
    def push(self,data):
        self.list.append(data)
        print(f"{data} is pushed to stack")
    def pop(self):
        if not self.is_empty():
            a=self.list.pop()
            print(f"{a} is poped from stack")
            return a

        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
           return self.list[-1]
        else:
            raise IndexError("Stack is empty")
    def size(self):
        print(len(self.list))
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
s1.size()
s1.peek()
s1.pop()
s1.size()