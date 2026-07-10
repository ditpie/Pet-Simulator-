#If all that behaves the way you expect, this base version is basically done. From here, a couple of natural next steps if you want to keep going:

# __init__ guard rails — right now nothing stops someone from creating Pet('Rex') with hunger already negative if you ever add init arguments later. Not urgent, just something to keep in mind as the pattern.
# A Cat subclass alongside Dog, and maybe a choice at the start of the program for which one to spawn.
# Stat decay over time — every loop iteration, hunger creeps up a little even without playing, so doing nothing has consequences.

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5

    def feed(self):
        self.hunger = max(0, self.hunger - 2)
        self.energy = min(10, self.energy + 2)
        self.happiness = min(10, self.happiness + 2)

    def play(self):
        self.hunger = min(10, self.hunger + 2)
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 3)

    def sleep(self):
        self.hunger = max(0, self.hunger - 2)
        self.energy = min(10, self.energy + 2)

    def status(self):
        print(f'''
{self.name} conditions are = 
Hunger : {self.hunger}
Energy : {self.energy} 
Happiness : {self.happiness}''')

#Inheritance
class Dog(Pet):
    def bark(self):
        print('Woof')

class Cat(Pet):
    def meow(self):
        print('Meow')

#Pets
pet1 = Pet('Cat')
pet2 = Pet('Dog')

#Code
while True:
    question = input('Which pet do you like to spawn (Cat/Dog)? ').capitalize()
    if question == 'Dog':
        pets = pet2
        break
    elif question == 'Cat':
        pets = pet1
        break
    else:
        print('Please enter a valid option')

print('============')

# Menu Loop
while True:
    try:
        print('''What do you want to do today?
feed
play
sleep
status 
quit
         ''')
        choice = input('Please choose an option: ')
        if choice == 'feed':
            if pets.hunger == 0:
                print(f'{pets.name} is already full!')
            else:
                pets.feed()
                print('Yummy!')
        elif choice == 'play':
            if pet1.energy <= 2:
                print(f'{pets.name} is tired!')
            else:
                pets.play()
                print('Wooho')
        elif choice == 'sleep':
            if pets.energy >= 9:
                print(f'{pets.name} is still active!')
            else:
                pets.sleep()
                print('Zzzzz')
        elif choice == 'status':
            pets.status()
        elif choice == 'quit':
            print('Goodbye!')
            break
        else:
            print('Please choose a valid option: ')
    except Exception as e:
        print("Something went wrong, try again")