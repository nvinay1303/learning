class Dog:
    def __init__(self, firstname, breed, owner):
            self.name = firstname
            self.breed = breed
            self.owner = owner

    def bark(self):
        print("Woof!")

class Owner:
     def __init__(self, name, address, contact):
          self.name = name
          self.address = address
          self.phone_no = contact
    
owner1 = Owner('nikhil', 'erlanger strasse 23', 1757697053)
dog1 = Dog('Arjun', 'rotweiler', owner1) # create a dog object and assign it to the variable dog
# dog1.bark() 
print(dog1.owner.address)

owner2 = Owner('aruni', 'chathannor', 292922323)
dog2 = Dog('Brea', 'poodle', owner2) # create another dog object and assign it to the variable dog2
# dog2.bark()
print(dog2.owner.address)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old")


person1 = Person('Nikhil', 34)
person1.greet()

person2 = Person("Aruni", 33)
person2.greet()

Person("Nitara", 2).greet()