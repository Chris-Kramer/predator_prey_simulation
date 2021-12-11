from parameters import Population
from typing import Type, Optional, Tuple

class Animal:
    """
    A generic animal in the simulation. See classes Fox and Rabbit.
    """
    def __init__(self, population: Population, patch: "Patch", energy: int, age = int):
        self.__population = population
        self._patch = patch
        self._energy = population.max_energy
        self._age = age
        self.__is_alive = True #Newly created animals should always be alive
    
    def age(self) -> int:
        """
        Returns the age of the animal. The value does not change after the death of the animal.
        """
        return self._age
    
    def can_reproduce(self) -> bool:
        """
        Returns True if the animal is alive, is old enough, and has enough energy to reproduce, False otherwise.
        """
        min_energy = self.population.reproduction_min_energy
        min_age = self.population.reproduction_min_age
        if self.is_alive() and self.energy() >= min_energy and self.age() >= min_age:
            return True
        else:
            return False
    
    def energy(self) -> bool:
        """
        Returns the energy of the animal. The value does not change after the death of the animal.
        """
        return self._energy
    
    def feed(self) -> None: 
        """
        Feeds itself using the resources at its current location.
        """
        raise NotImplementedError # Will be implemented by subclasses
    
    def is_alive(self) -> bool:
        """
        Returns True if the animal is alive, False otherwise.
        """
        return self.__is_alive
    
    def move_to(selv, patch: "Patch") -> bool:
        """
        If the animal is alive, it goes from its current patch to the given one. Patches are updated accordingly.
        MOCK IMPLEMENTATION
        """
        print("MOCK IMPLEMENTATION")
    
    def patch(self) -> "Patch":
        """
        Returns the position of the animal. The value does not change after the death of the animal.
        """
        return self._patch
    
    def predator_in(self, patch: "Patch") -> bool:
        """
        Returns True if the given patch contains a alive predator of this animal.
        """
        raise NotImplementedError # Will be implemented by subclasses
    
    def reproduce(self, newborn_patch: "Patch") -> Optional["Animal"]:
        """
        If the animal is alive, it tries to reproduce using the patch provided. Returns an instance for the newborn (located at newborn_patch) or None. Patches are updated accordingly.
        MOCK IMPLEMENTATION
        """
        if self.is_alive():
            newborn = Animal(population = self.__population, #Same species as parent
                             patch = newborn_patch,
                             energy = self.__population.max_energy, # I figured that all newborns have max energy, however this implementation is debateable
                             age = 0)
            return newborn
    
    def same_species_in(self, patch: "Patch") -> bool:
        """
        Return True if the given patch contains an alive animal of the same species.
        """
        for animal in patch.animals(): 
            if animal.__population.species == self.__population.species:
                return True
        else:
            return False
    
    def tick(self):
        """
        Records the passage of time (one step in the simulation). If the animal is alive, it ages and consumes its energy. If the animal becomes too old or depletes its energy reserve, it dies and it is removed from its current patch.
        """
        if self.is_alive():
            self._age += 1
            self._energy -= self.__population.metabolism
            # Set animal to dead if conditions are met
            max_age = self.__population.max_age
            if self.age() >= max_age or self.energy() <= 0:
                self.__is_alive = False

                animal = self
                self.patch().remove(animal)
    
    # These methods for representation are most likely unnecessary, but they are created just in case
    # __str__ is not used, since it defaults to __repr__ if not defined
    def __repr__(self) -> str:
        return ( f"Animal:\n"
                 f"population = {self.__population.species}\n "
                 f"patch = {self.patch()}\n "
                 f"energy = {self.energy()}\n "
                 f"age = {self.age()})\n "
                 f"Alive = {self.is_alive()}")  
    

class Patch:
    """
    """
    def __init__(self, x: int, y = int):
        self._x = x
        self._y= y

    def add(self, animal: "Animal") -> None:
        print("MOCK IMPLEMENATION")
    
    def animals(self) -> None:
        print("MOCK IMPLEMENATION")
    
    def coordinates(self) -> Tuple[int, int]:
        print("MOCK IMPLEMENATION")
    
    def grass(self) -> int:
        print("MOCK IMPLEMENATION")
    
    def has_alive_rabbit(self) -> bool:
        print("MOCK IMPLEMENATION")
    
    def remove(self, animal) -> None:
        print("MOCK IMPLEMENATION")
    
    def tick(self) -> None:
        print("MOCK IMPLEMENATION")

if __name__ == "__main__":
    #pass
    import parameters as params
    import random
    pop = Population('foxes',
                        25,  # initial_size
                        2,   # metabolism
                        50,  # max_age
                        200, # max_energy
                        .5,  # reproduction_rate
                        120, # reproduction_min_energy
                        10,  # reproduction_min_age
                        )
    animals = []
    for i in range(50):
        patch = Patch(10,10)
        animal = Animal(population=pop,
                        patch=patch,
                        energy=144,
                        age = random.randint(1, pop.max_age))
        animals.append(animal)
        #print(animal)
    for i in range(1000):
        for animal in animals:
            animal.tick()