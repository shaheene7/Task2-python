class Dog():
    def speak(self):
        print("Dog says: Woof! 🐶")

    def move(self):
        print ("Dog runs in the yard.")
    
class Cat():

    def speak(self):
       print("Cat says: Meow! 🐱")
    
    def move(self):
       print("Cat climbs the tree.")    

class Bird():

    def speak(self):
        print("Bird says: Tweet! 🐦")
    
    def move(self):
        print("Bird flies in the sky.")

class Fish():

    def speak(self):
        print("Fish says: Blub! 🐠")
    
    def move(self):
        print("Fish swims in the tank.")

def create_animal(animal_type):
    pets = dict(
        dog=Dog(),cat=Cat(),fish=Fish(),bird=Bird()
        )
    return pets[animal_type] 

        

while True:
    animal_type = input("Enter the type of animal (dog, cat, bird, fish) or 'q' to quit: ").strip().lower()
    if animal_type == 'q':
        break
    try:
        animal = create_animal(animal_type)
        animal.speak()
        animal.move()
    except KeyError:
        print("Unknown animal type. Please try again.")


""" I use Factory pattern because the object created in run time based on the user input
    and the most pattern satisfies this is Factory pattern."""

