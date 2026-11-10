'''
class Car:

    def __init__(self, weight, name, horsepower):
        self.name = name
        self.weight = weight
        self.horsepower = horsepower

    def engine(self):
        return "Rrrrrrrr"

t = Car(1000, 'Avtomobil', 300)
print(t.horsepower)
print(t.engine())
'''

class Node:

    def __init__(self, value):
        self.value = value
        self.heightLeft = 0
        self.heightRight = 0
        self.left = None # узел -- левый потомок
        self.right = None # узел -- правый потомок

    def heightCalc(self):
        if self.left != None:
            self.heightLeft = max(self.left.heightLeft, self.left.heightRight) + 1
        if self.right != None:
            self.heightRight = max(self.right.heightLeft, self.right.heightRight) + 1

    def diffCalc(self):
        return self.heightLeft - self.heightRight

    def balance(self):
        pass

    def rotateLeft(self):
        b = self.right
        self.right = b.left
        b.left = self

    def rotateRight(self):
        b = self.left
        self.left = b.right
        b.right = self

    def bigRotateLeft(self):
        self.right.rotateRight()
        self.rotateLeft()

    def bigRotateRight(self):
        self.left.rotateLeft()
        self.rotateRight()

a = Node(5)
b = Node(7)
c = Node(6)
d = Node(1)
e = Node(5.5)
f = Node(6.5)
g = Node(10)

a.left = d
a.right = b
b.left = c
b.right = g
c.left = e
c.right = f

print(a.right.left.left.value)

a.bigRotateLeft()

print(c.right.value)

