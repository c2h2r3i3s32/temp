class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.arr[self.rear] = item
        self.size += 1
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        item = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"Dequeued: {item}")
        return item

    def front_element(self):
        if self.is_empty():
            print("Queue is empty. No front element.")
            return None
        return self.arr[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue elements:", end=" ")
        index = self.front
        for i in range(self.size):
            print(self.arr[index], end=" ")
            index = (index + 1) % self.capacity
        print()

queue = ArrayQueue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)  
queue.display()
print("Front element:", queue.front_element())

queue.dequeue()
queue.dequeue()

queue.display()

queue.enqueue(60)
queue.display()

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()  
queue.display()

