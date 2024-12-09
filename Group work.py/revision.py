class Animal:
    def speak(self):
        print("This animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("The dog barks")


dog =Dog( )
dog.speak()


class Parent:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self._private = "Private"


class Child(Parent):
    def display(self):
        print(self.public)
        print(self._protected)


child = Child( )
child.display( )                
