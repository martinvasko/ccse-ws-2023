class ParentClass:
    def printHello(self):
        print("Hello, World")


class ChildClass(ParentClass):
    def someNewMethod(self):
        print("ParentClass objects don't have this method")


class GrandchildClass(ChildClass):
    def anotherNewMethod(self):
        print("Only GrandchildClass objects have this method")
