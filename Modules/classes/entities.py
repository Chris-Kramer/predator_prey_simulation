from parameters import Population
import random
from typing import List, Type, Optional, Tuple

class Animal:
    """
    A generic animal in the simulation. See classes Fox and Rabbit.
    """
    def __init__(self, population: Population, patch: "Patch", energy: int, age: int):
        patch.add(self)
        self._population = population
        self._patch = patch
        self._energy = energy
        self._age = age
    
    def age(self) -> int:
        """
        Returns the age of the animal. The value does not change after the death of the animal.
        """
        return self._age
    
    def can_reproduce(self) -> bool:
        """
        Returns True if the animal is alive, is old enough, and has enough energy to reproduce, False otherwise.
        """
        min_energy = self._population.reproduction_min_energy
        min_age = self._population.reproduction_min_age
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
        raise NotImplementedError # Will be implemented by subclasses
    
    def move_to(self, patch: "Patch") -> None:
        """
        If the animal is alive, it goes from its current patch to the given one. Patches are updated accordingly.
        """
        animal = self
        animal.patch().remove(animal)
        patch.add(animal)
        animal._patch = patch

    def patch(self) -> "Patch":
        """
        Returns the position of the animal. The value does not change after the death of the animal.
        """
        return self._patch
    
    def predators_in(self, patch: "Patch") -> bool:
        """
        Returns True if the given patch contains a alive predator of this animal.
        """
        raise NotImplementedError # Will be implemented by subclasses
    
    def reproduce(self, newborn_patch: "Patch", rep_cost_rate: float) -> Optional["Animal"]:
        """
        If the animal is alive, it tries to reproduce using the patch provided.
        Returns an instance for the newborn (located at newborn_patch) or None.
        Patches are updated accordingly.
        """
        raise NotImplementedError # Will be implemented by subclasses
    
    def same_species_in(self, patch: "Patch") -> bool:
        """
        Return True if the given patch contains an alive animal of the same species.
        """
        for animal in patch.animals(): 
            if animal._population.species == self._population.species:
                return True
            else:
                return False
    
    def tick(self):
        """
        Records the passage of time (one step in the simulation).
        If the animal is alive, it ages and consumes its energy.
        If the animal becomes too old or depletes its energy reserve, it dies and it is removed from its current patch.
        """
        if self.is_alive():
            self._age += 1
            self._energy -= self._population.metabolism
            # Set animal to dead if conditions are met
            max_age = self._population.max_age
            if self.age() >= max_age or self.energy() <= 0:
                animal = self #This is done to avoid confusion between self referring to the animal or the patch
                animal.patch().remove(animal)
    
    # _str_ is not used, since it defaults to _repr_ if not defined
    def __repr__(self) -> str:
        return ( f"\nAnimal:\n " 
                 f"  Population = {self._population.species}\n "
                 f"  Patch coords = {self.patch().coordinates()}\n "
                 f"  Energy = {self.energy()}\n "
                 f"  Age = {self.age()}\n "
                 f"  Alive = {self.is_alive()}")  


# ----- Animal subclass: Fox -----
class Fox(Animal):
    def __init__(self, patch: "Patch", population):
        patch.add(self)
        self._population = population
        self._patch = patch


# ------ Animal subclass: Rabbit -----
class Rabbit(Animal):
    reproduction_cost_rate = 0.85
    feeding_metabolism_rate = 2.5

    def __init__(self, population: Population, patch: "Patch", age:int):
        # Initialise attributes
        self._energy = int(population.max_energy * 0.25)
        self._population =  population
        self._patch = patch
        self._age = age
        self._was_killed = False
        # Inherit from Superclass Animals
        super().__init__(population = self._population,
                         patch = self._patch,
                         energy = self._energy,
                         age = self._age)
    def kill(self):
        rabbit = self
        rabbit.patch().remove(rabbit)
        rabbit._was_killed = True
        
    def was_killed(self)-> bool:
        return self._was_killed 

    def is_alive(self) -> bool:
        if self._energy > 0 and self._age < self._population.max_age and self._was_killed == False:
            return True
        else:
            return False
    
    def feed(self):
        if self.is_alive():
            # Determine how much grass the rabbit can eat
            grass_amount = self.patch().grass() 
            grass_eaten =  Rabbit.feeding_metabolism_rate * self._population.metabolism
            if grass_amount - grass_eaten < 0:
                grass_eaten = grass_amount
                grass_amount = 0
            if self._energy + grass_eaten > self._population.max_energy:
                grass_eaten = self._population.max_energy - self._energy
            # Update values
            self._energy += grass_eaten
            self.patch()._patch_grass -= grass_eaten

    def reproduce(self, newborn_patch: "Patch") -> Optional["Rabbit"]:
        if self.can_reproduce() and self.is_alive():
            probability = self._population.reproduction_probability
            reproduction_res = random.random()
            if reproduction_res <= probability:
                self._energy -= self._population.reproduction_min_energy * Rabbit.reproduction_cost_rate
                rabbit = Rabbit(population = self._population,
                                patch = newborn_patch,
                                age = 0)
                return rabbit
        
# predators in
    def predators_in(self, patch: "Patch") -> bool:
        predator = False
        for animal in patch.animals():
            if isinstance(animal, Fox):
                predator = True
        return predator


class Patch:
    """
    A patch of grass at a given pair of coordinates.

    x: the west-east corrdinate for this patch.
    y: the north-south coordinate for this patch.
    """
    min_grass_growth = 1
    max_grass_growth = 4
    max_grass_amount = 30
    def __init__(self, x: int, y = int):
        self._x = x
        self._y= y
        self._animals = []
        self._patch_grass = random.randint(0, self._max_grass_amount)

    def coordinates(self) -> Tuple[int, int]:
        """Method for returning the coordinates of the patch.
        
        Returns
        -------
        self.coords (x: west east coordinate, y: north south coordinate)
        
        """
        return (self._x, self._y)
        
    def grass(self) -> int:
        """Method for returning the amount of grass in a patch.
        Returns
        -------
        An integer of how much grass in the patch
        """
        return self._patch_grass

    def tick(self) -> None:
        """Method for recording the passage of time (one step in the simulation) -> Grass grows.
        Returns
        -------
        Nothing. 
        """
        if self.grass() <= Patch.max_grass_amount:
            self._patch_grass += random.randint(Patch.min_grass_growth, Patch.max_grass_growth)
        
    def animals(self) -> List[Animal]:
        """Method for returning a list of animals in the patch.
        Returns
        -------
        list of animals in a patch. 
        """
        return self._animals
        
    def has_alive_fox(self) -> bool:
        for animal in self._animals:
            if isinstance(animal, Fox) and animal.is_alive():
                return True
            else:
                return False

    def has_alive_rabbit(self) -> bool:
        for animal in self._animals:
            if isinstance(animal, Rabbit) and animal.is_alive():
                return True
            else:
                return False
        
    def add(self, animal: "Animal") -> None:
        self._animals.append(animal)

    def remove(self, animal) -> None:
        self._animals.remove(animal)

    # __str__ is not used, since it defaults to __repr__ if not defined
    def __repr__(self) -> str:
        return ( f"Patch:\n"
                 f"Coordinates = {self.coordinates()}\n "
                 f"Grass_amount = {self._patch_grass}\n "
                 f"Animals = {self._animals}\n ")

 
if __name__ == "__main__":
    #pass
    import parameters as params
    import random
    pop = Population('rabbits',
                        25,  # initial_size
                        3,   # metabolism
                        100,  # max_age
                        50, # max_energy
                        .5,  # reproduction_rate
                        2, # reproduction_min_energy
                        1,  # reproduction_min_age
                        )
    popF = Population('foxes',
                        25,  # initial_size
                        3,   # metabolism
                        100,  # max_age
                        50, # max_energy
                        .5,  # reproduction_rate
                        2, # reproduction_min_energy
                        1,  # reproduction_min_age
                        )    
    animals = []
    patch = Patch(1, 1)
    patch_pred = Patch(2,2)
    fox = Fox(patch_pred, popF)
    patch_2 = Patch(random.randint(1, 30), random.randint(1, 30))
    for i in range(2):
        rabbit = Rabbit(population=pop,
                        patch=patch,
                        age = random.randint(0, 30))
        animals.append(rabbit)
        print(rabbit)
    for i in range(100):
        rabbit.tick()
        rabbit.feed()
        print(rabbit)