class Cir_Que():

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    # Add element into the queue
    def enque(self, elem):

        if ((self.rear + 1) % self.size == self.front):
            print "Circle queue is overfull\n"

        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = elem
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = elem

    # Remove element from the queue
    def deque(self):
        if (self.front == -1):
            print "Circle queue is empty\n"

        elif (self.front == self.rear):
            ext = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return ext
        else:
            ext = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return ext

    def print_Que(self):
        if(self.front == -1):
            print "Circle queue is empty"

        elif (self.rear >= self.front):
            for i in xrange(self.front, self.rear + 1):
                print self.queue[i],
            print
        else:
            for i in xrange(self.front, self.size):
                print self.queue[i],
            for i in xrange(0, self.rear + 1):
                print self.queue[i],
            print


# test
# Initialisation Cir_Que:
# cq_1 = Cir_Que(5)
# cq_1.enque(1)
# cq_1.enque(2)
# cq_1.enque(3)
# cq_1.enque(4)
# cq_1.enque(5)
# print "Initial queue"
# cq_1.print_Que()
# cq_1.deque()
# print "After remove elem from the queue"
# cq_1.print_Que()
# cq_1.deque()
# cq_1.deque()
# print "After remove elem from the queue"
# cq_1.print_Que()
# cq_1.enque(10)
# cq_1.enque(20)
# print "Actual queue"
# cq_1.print_Que()
# cq_1.enque(30)
# cq_1.enque(40)
# cq_1.enque(50)
# print "Actual queue"
# cq_1.print_Que()
# cq_1.enque(30)
# cq_1.enque(40)
# cq_1.enque(50)
# cq_1.enque(60)
# cq_1.enque(70)
# print "Actual queue"
# cq_1.print_Que()
# cq_1.enque(100)