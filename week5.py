#1
classRectangle:
def init (self,color="green",width=100,height=100):self.color = color
self.width = widthself.height = height
defsquare(self): 3
returnself.width *self.height
rect1 = Rectangle()
print(rect1.color)
print(rect1.square())
rect1 = Rectangle("yellow",23,34)
print(rect1.color)
print(rect1.square())


#2
class name():
    def __init__(self,first_name,last_name,full_name):
        self.first_name=first_name
        self.last_name=last_name
        self.full_name=full_name
    def prt(self):
        print('My full name is ' + self.full_name +'.I am 19 years old,', 'call me just '+self.first_name)
Stundent=name('Nurbek','Kydyraliev','Nurbek Kydyraliev')
Stundent.prt()



#3
class cal():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def mul(self):
        return self.x * self.y
    def div(self):
        return self.x / self.y
    def sub(self):
        return self.x - self.y
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
obj = cal(x, y)
choice = 1
while choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Result: ", obj.add())
    elif choice == 2:
        print("Result: ", obj.sub())
    elif choice == 3:
        print("Result: ", obj.mul())
    elif choice == 4:
        print("Result: ", round(obj.div(), 2))
    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
print()