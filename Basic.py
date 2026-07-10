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
        self.hunger = max(0, self.hunger - 2)
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

#Pets
pet1 = Dog('Shiba')


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
            if pet1.hunger == 0:
                print(f'{pet1.name} is already full!')
            else:
                pet1.feed()
                print('Yummy!')
        elif choice == 'play':
            if pet1.energy <= 2:
                print(f'{pet1.name} is tired!')
            else:
                pet1.play()
                print('Wooho')
        elif choice == 'sleep':
            pet1.sleep()
            if pet1.energy >= 9:
                print(f'{pet1.name} is still active!')
            else:
                pass
        elif choice == 'status':
            pet1.status()
        elif choice == 'quit':
            print('Goodbye!')
            break
        else:
            print('Please choose a valid option: ')
    except Exception as e:
        print("Something went wrong, try again")