class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        self.energy = min(10, self.energy + 5)

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f'{self.name} learned a new trick: {trick}!')
        else:
            print(f'{self.name} already knows the trick: {trick}.')

    def show_tricks(self):
        if self.tricks:
            print(f'{self.name} knows the following tricks:')
            for trick in self.tricks:
                print(f'- {trick}')
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        print(f"Pet Name: {self.name}")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

first_pet = Pet('Tiger')
first_pet.eat()
first_pet.play()
first_pet.sleep()
first_pet.get_status()
first_pet.train('Jump')
first_pet.show_tricks()