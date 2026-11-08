class SuperHero:
    def __init__(self, name: str, health: int, power_level: int):
        self.name = name
        self.__health = health
        self.__power_level = power_level
    
    # TODO: Add the getter and setter methods
    # Remember to use the @property decorator for the getter methods
    # Remember to use the @setter decorator for the setter methods

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, new_Health):
        if new_Health > 100:
            print("You can't set the health to more than 100")
        elif new_Health < 0:
            print("You can't set the health to less than 0")
        else:
            self.__health = new_Health
    
    @property
    def power(self):
        return self.__power_level
    
    @power.setter 
    def power(self, new_Power):
        if new_Power > 10:
            print("You can't set the power level to more than 10")
        elif new_Power < 1:
            print("You can't set the power level to less than 1")
        else: 
            self.__power_level = new_Power

# Don't change the following code
super_hero = SuperHero("Batman", 80, 9)

print(super_hero.health) # this should print 80
super_hero.health = 110 # this should print You can't set the health to more than 100

print(super_hero.power) # this should print 9
super_hero.power = 100 # this should print You can't set the power level to more than 10
super_hero.power = 0 # this should print You can't set the power level to less than 1
print(f"{super_hero.name} has {super_hero.health} health and {super_hero.power} power level")

# TODO: print the hero's attributes 
