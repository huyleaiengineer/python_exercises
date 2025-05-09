class Example:
    def __init__(self):
        self.name = ""

    def getString(self):
        self.name = input("Enter string = ")

    def printString(self):
        print(self.name.upper())


x = Example()

x.getString()
x.printString()
