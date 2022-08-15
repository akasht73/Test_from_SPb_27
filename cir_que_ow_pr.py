class Cir_Que_pri():
    def __init__(self, size):
        self.size = size
        self.queue = [(0, 0)] * size
        self.front = self.rear = -1

    # Add element into the queue
    def enque(self, id, priority=False):

        article = (id, priority)

        if ((self.rear + 1) % self.size == self.front):
            temp = self.__select_prior()
            if temp == self.queue[self.front]:
                self.front = (self.front + 1) % self.size
                self.rear = (self.rear + 1) % self.size
                self.queue[self.rear] = article
                print "Frontal element {} overwrited new element {}".format(temp[0], article[0])
            elif temp == self.queue[self.rear]:
                self.queue[self.rear] = article
                print "Priority element {} overwrited new element {}".format(temp[0], article[0])
            else:
                for i in xrange(self.queue.index(temp) + 1, self.size):
                    self.queue[i] = self.queue[(i + 1) % self.size]
                for i in xrange(self.front):
                    self.queue[i] = self.queue[(i + 1) % self.size]
                print "Priority element {} overwrited new element {}".format(temp[0], article[0])

        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = article
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = article

    # Remove element from the queue
    def deque(self):
        if self.front == -1:
            print "Circle queue is empty\n"
        elif (self.front == self.rear):
            ext = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return ext[0]
        else:
            ext = self.__select_prior()
            if self.queue.index(ext) == self.front:
                self.front = (self.front + 1) % self.size
            elif self.queue.index(ext) == self.rear:
                self.rear = (self.rear - 1) % self.size
            else:
                if self.rear > self.front:
                    for i in xrange(self.queue.index(ext), self.rear + 1):
                        self.queue[i] = self.queue[(i + 1) % self.size]
                    self.rear = (self.rear - 1) % self.size
                elif self.queue.index(ext) < self.rear:
                    for i in xrange(self.queue.index(ext), self.rear + 1):
                        self.queue[i] = self.queue[(i + 1) % self.size]
                    self.rear = (self.rear - 1) % self.size
                else:
                    for i in xrange(self.queue.index(ext), self.size):
                        self.queue[i] = self.queue[(i + 1) % self.size]
                    for i in xrange(self.rear + 1):
                        self.queue[i] = self.queue[(i + 1) % self.size]
                    self.rear = (self.rear - 1) % self.size

            return ext[0]

    # Select element to be overwritten
    def __select_prior(self):  # return whole tuple
        if self.rear > self.front:
            for i in xrange(self.front, self.rear + 1):
                if self.queue[i][1]:
                    return self.queue[i]
                continue
            return self.queue[self.front]
        elif self.rear < self.front:
            for i in xrange(self.front, self.size):
                if self.queue[i][1]:
                    return self.queue[i]
                continue
            for i in xrange(self.rear + 1):
                if self.queue[i][1]:
                    return self.queue[i]
                continue
            return self.queue[self.front]

    def print_Que(self):
        if self.front == -1:
            print "Circle queue is empty\n"
        elif self.rear >= self.front:
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
# Initialisation Cir_Que_pri:
# cq_pri = Cir_Que_pri(8)
# cq_pri.enque(1)
# cq_pri.enque(2)
# cq_pri.enque(3, True)
# cq_pri.enque(4)
# cq_pri.enque(5)
# print "initial queue"
# cq_pri.print_Que()
# print cq_pri.queue
# cq_pri.enque(6)
# cq_pri.enque(7, True)
# cq_pri.enque(8)
# cq_pri.deque()
# print "After remove elem from the queue"
# cq_pri.print_Que()
# print cq_pri.queue
# print cq_pri.deque()
# print cq_pri.deque()
# print cq_pri.deque()
# print "After remove elem from the queue"
# cq_pri.print_Que()
# print cq_pri.queue
# cq_pri.enque(10)
# cq_pri.enque(20)
# print "Actual queue"
# cq_pri.print_Que()
# print cq_pri.queue
# cq_pri.enque(30)
# cq_pri.enque(40, True)
# cq_pri.enque(50)
# print "Actual queue"
# cq_pri.print_Que()
# print cq_pri.queue
# cq_pri.enque(130)
# cq_pri.enque(140, True)
# cq_pri.enque(50)
# cq_pri.enque(60)
# cq_pri.enque(70, True)
# print "Actual queue"
# cq_pri.print_Que()
# print cq_pri.queue
# cq_pri.enque(100)
