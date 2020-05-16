# basic class structure of queue using python list


class Queue:
    def __init__(self):
        self.queue_list = []

    def front(self):
        if self.is_empty():
            return None
        return self.queue_list[0]

    def back(self):
        if self.is_empty():
            return None
        return self.queue_list[-1]

    def is_empty(self):
        return len(self.queue_list) == 0

    def size(self):
        return len(self.queue_list)

    # append value at the end of the list
    def enqueue(self, value):
        self.queue_list.append(value)

    # dequeue operation removes and return first element
    def dequeue(self):
        if self.is_empty():
            return None
        front = self.queue_list.remove(self.front())
        return front


queue = Queue()

print("queue.enqueue(2);")
queue.enqueue(2)
print("queue.enqueue(4);")
queue.enqueue(4)
print("queue.enqueue(6);")
queue.enqueue(6)
print("queue.enqueue(8);")
queue.enqueue(8)
print("queue.enqueue(10);")
queue.enqueue(10)

print("Dequeue(): " + str(queue.dequeue()))
print("Dequeue(): " + str(queue.dequeue()))

print("front(): " + str(queue.front()))
print("back(): " + str(queue.back()))

queue.enqueue(12)
queue.enqueue(14)

while queue.is_empty() == False:
    print("Dequeue(): " + str(queue.dequeue()))
print("isEmpty(): " + str(queue.is_empty()))

