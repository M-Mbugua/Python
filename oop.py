class Dog():

    # CLASS OBJECT ATTRIBUTE
    # sAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'

    def __init__(self,breed,name,spots):

        self.breed = breed
        self.name = name
        self.spots = spots


    def bark(self, number):
        print(f'Woof! My name is {self.name} and the number is {number}.')



class Circle():

    # CLASS OBJECT ATTRIBUTE
    pi = 3.142

    def __init__(self, radius=1):

        self.radius = radius

    # METHOD
    def circumference(self):
        return self.radius * self.pi * 2
        # return self.radius ^ Circle.pi * 2



class Animal():

    def __init__(self):
        print('Animal created')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')


class Cat(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Cat created')

    def who_am_i(self):
        print('I am a cat!')


class Calf():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says moo!"


class Duck():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says quack!"


# BASE CLASS: NOT INSTANTIATED
class Animal():

    def __init__(self, name):
        self.name = name

    # EXCPECTED TO OVERRIDE IN CHILD CLASS
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


class Book():

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted.")













