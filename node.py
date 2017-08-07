#Binod Bhandari
#Drexel University 2017
#CS 260-002Summer 2017

class Node:

    def __init__(self,value,next=None):

        self.value = value
        self.next = next

    def __str__(self):
        result = "[ "+str(self.value)+ " ]"
        return result

    def getNext(self):
        return self.next

    def setNext(self,next):
        self.next = next

    def getValue(self):
        return self.value

    def setValue(self,value):
        self.value = value
