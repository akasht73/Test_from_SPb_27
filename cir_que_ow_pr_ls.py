class Cir_Que_pri_lst_bl:
    def __init__(self, size):
        self.size = size
        self.simples = []
        self.priors = []
        self.order = 0

    def enque(self, id, priority = False):
        self.order += 1
        article = {
            "id": id,
            "priority": priority,
            "order": self.order
        }
        if len(self.simples) + len(self.priors) < self.size:
            if priority:
                self.priors.append(article)
            else:
                self.simples.append(article)

        else:
            if priority:
                self.priors.append(article)
                return self.priors.pop(0)
            else:
                self.simples.append(article)
                if len(self.priors) > 0:
                    return self.priors.pop(0)
                return self.simples.pop(0)

    def deque(self):
        if len(self.simples) + len(self.priors) == 0:
            print "Circle queue is empty\n"
        elif len(self.priors) == 0:
            return self.simples.pop(0)
        return self.priors.pop(0)

    def print_Que(self):
        result = self.priors + self.simples
        print sorted(result, key=lambda art: art["order"])


# # test
# # Initialisation Cir_Que_pri_lst_bl:
# cq_pri_d = Cir_Que_pri_lst_bl(8)
# cq_pri_d.enque(1)
# cq_pri_d.enque(2)
# cq_pri_d.enque(3, True)
# cq_pri_d.enque(4)
# cq_pri_d.enque(5)
# print "initial queue"
# cq_pri_d.print_Que()
# print cq_pri_d.priors + cq_pri_d.simples
# cq_pri_d.enque(6)
# cq_pri_d.enque(7, True)
# cq_pri_d.enque(8)
# cq_pri_d.deque()
# print "After remove elem from the queue"
# cq_pri_d.print_Que()
# print cq_pri_d.priors + cq_pri_d.simples
# print(cq_pri_d.deque())
# print(cq_pri_d.deque())
# print(cq_pri_d.deque())
# print "After remove elem from the queue"
# cq_pri_d.print_Que()
# print cq_pri_d.priors + cq_pri_d.simples
# cq_pri_d.enque(10)
# cq_pri_d.enque(20)
# print "Actual queue"
# cq_pri_d.print_Que()
# print cq_pri_d.priors + cq_pri_d.simples
# cq_pri_d.enque(30)
# cq_pri_d.enque(40, True)
# cq_pri_d.enque(50)
# print "Actual queue"
# cq_pri_d.print_Que()
# print cq_pri_d.priors + cq_pri_d.simples
# cq_pri_d.enque(130)
# cq_pri_d.enque(140, True)
# cq_pri_d.enque(50)
# cq_pri_d.enque(60)
# cq_pri_d.enque(70, True)
# print "Actual queue"
# cq_pri_d.print_Que()
# print cq_pri_d.priors + cq_pri_d.simples
# cq_pri_d.enque(100)