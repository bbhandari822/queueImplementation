#Binod Bhandari
#Drexel University 2017
#CS 260-002Summer 2017
from node import *

class Queue:

    def __init__(self):

        self.head= None
        self.current = self.head
        self.size = 0

    def __str__(self):
#checks if the queue is empty and return all the elements if not
        if self.empty():
            return "Queue Empty"
        else:
            new = self.head
            return_res = ""
            while (new.getNext() != None):
                return_res += str(new.getNext)
            return_res = return_res+ str(new)
            return return_res

    def empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def front(self):
        if self.empty() == True:
            return self.empty()
        else:
            return self.head.getValue()

    def enqueue(self,x):

        myQueue = Node(x)
        if (self.size==0):
            self.head = self.current = myQueue
        else:
            self.current.next = myQueue
            self.current = myQueue
        self.size = self.size+1

    def dequeue(self):

        if self.empty() != True:
            x = self.head
            self.head = self.head.next
            self.size = self.size - 1
            return x.value
        else:
            return self.empty()

    def size(self):
        return self.size