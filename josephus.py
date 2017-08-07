#Binod Bhandari
#Drexel University 2017
#CS 260-002Summer 2017

import sys
from queue import *

# this code is incomplete, it just print the first element of josephus number.
def josephus():
    circle_queue = Queue()

    #takes optional argument
    n = sys.argv[1]
    m= sys.argv[2]

    #stores value of i in a queue
    for i in range(int(n)):
        circle_queue.enqueue(i)
    j = 0
    while (j < int(m)-1):
        #dequeue the element at position m and enqueue the rest and again dequeue the remaining
        circle_queue.enqueue(circle_queue.dequeue())
        j += 1
    print(circle_queue.dequeue()) #just print the first elements

josephus() # calling the method.