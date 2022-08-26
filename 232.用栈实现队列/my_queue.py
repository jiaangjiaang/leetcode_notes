class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            return self.stack1[0]
        else:
            return self.stack2[-1]

    def empty(self) -> bool:
        if not self.stack1 and not self.stack2:
            return True
        else:
            return False

def main():
    my_queue = MyQueue()
    my_queue.push(1)
    my_queue.push(2)
    my_queue.push(3)
    my_queue.push(4)
    print(my_queue.pop())
    my_queue.push(5)
    print(my_queue.pop())
    print(my_queue.pop())
    print(my_queue.pop())
    print(my_queue.pop())

if __name__ == '__main__':
    main()