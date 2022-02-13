from parameters import Population
import random
from typing import List, Optional, Tuple

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
        if self.is_alive() == False:
            animal = self #This is done to avoid confusion between self referring to the animal or the patch
            animal.patch().remove(animal)
        else:
            self._age += 1
            self._energy = self.energy() - self._population.metabolism
            # Set animal to dead if conditions are met
            if self.is_alive() == False:
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
    """ A fox in the simulated world.

    Ancestors
    --------
    Animal

    Parameters
    ----------
    - population: The parameters for the fox population used in this run of the simulation.
    - patch: The position assigned to this animal (the constructor takes care of adding it to the list of animals of this patch).
    - Age: The current age of the animal

    Class variables
    ---------------
    - food_energy_per_unit: How much energy a fox gains when eating a rabbit
    - reproduction_cost_rate: The cost of reproduction as a percentage og the minimum reproduction level
    """
    reproduction_cost_rate = 0.85
    food_energy_per_unit = 15
    
    def __init__(self, population : Population, patch: "Patch", age:int):
        self._energy = int(population.max_energy * 0.70)
        self._population = population
        self._patch = patch
        self._age = age
        self._was_killed = False
        super().__init__(population = self._population,
                         patch = self._patch,
                         energy = self._energy,
                         age = self._age)

    def is_alive(self) -> bool:
        """
        Checks if the energy reserve of this animal is not depleted and that its age is below the max age for foxes. 

        Return
        -------
        A bool indicating if the animal is alive
        """
        if self._energy > 0 and self._age < self._population.max_age:
            return True
        else:
            return False
    
    def feed(self):
        """Feed this fox with a rabbit from its current patch, if the fox is alive, its
        energy reserve is not full, and in a patch with an alive rabbit.
        The rabbit is killed (see method kill of class Rabbit). A unit of food (one rabbit) provides food_energy_per_unit units
        of energy which are added to the energy reserve of this fox up to the maximum level possible. 
        Extra energy is ignored
        """
        animals = self.patch().animals()
        if self.is_alive() and self.energy() < self._population.max_energy and self.patch().has_alive_rabbit():
            for animal in animals:
                if isinstance(animal, Rabbit):
                    if Fox.food_energy_per_unit + self.energy() > self._population.max_energy:
                        self._energy = self._population.max_energy
                        animal.kill()
                    else:
                        self._energy += Fox.food_energy_per_unit 
                        animal.kill()
                
    def reproduce(self, newborn_patch: "Patch") -> Optional["Fox"]:
        """ Returns an instance of this class when successful and reduces the energy reserve of this animal 
        by the minimum energy requirement for reproduction multiplied by reproduction_cost_rate.

        Parameters
        ----------
        newborn_patch: An instance of the class Patch, where a potential newborn animal can spawn.

        Return
        -------
        An instance of this class with age zero located at the provided Patch.
        """
        if self.can_reproduce() and self.is_alive():
            probability = self._population.reproduction_probability
            reproduction_res = random.random()
            if reproduction_res <= probability:
                self._energy -= (self._population.reproduction_min_energy * Fox.reproduction_cost_rate)
                fox = Fox(population = self._population,
                                patch = newborn_patch,
                                age = 0)
                # If animal dies after reproduction, remove it
                if self.is_alive() == False:
                    animal = self #This is done to avoid confusion between self referring to the animal or the patch
                    animal.patch().remove(animal)
                return fox

    def predators_in(self, patch: "Patch") -> bool:
        """ Check of there are predators in a given Patch.
        
        Parameters
        ----------
        - patch: An instance of the class Patch.

        Return
        ------
        A bool indicating if there are a predator of this animal in the given patch.
        """
        return False


# ------ Animal subclass: Rabbit -----
class Rabbit(Animal):
    """ A rabbit in the simulated world.
    
    Parameters
    ----------
    - population: The parameters for the rabbit population used in this run of the simulation.
    - patch: The parameters for the rabbit population used in this run of the simulation.
    - age: The current age of the animal

    Ancestors
    ---------
    - Animal

    Class variables
    ----------------
    - reproduction_cost_rate: The cost of reproduction as a percentage og the minimum reproduction level
    - feeding_metabolism_rate: A percentage of how much of a rabbits metabolism it can use for feeding
    """
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
        """ Kill this rabbit and remove it from the current patch, if this rabbit is alive.
        """
        rabbit = self
        rabbit.patch().remove(rabbit)
        rabbit._was_killed = True
        
    def was_killed(self)-> bool:
        """Check if this rabbit was killed.
        
        Return
        -------
        A bool indicating if this rabbit was killed
        """
        return self._was_killed 

    def is_alive(self) -> bool:
        """Checks if the energy reserve of this animal is not depleted, 
        if its age is below the age limit (same as foxes), and if this rabbit was not killed.
        
        Return
        -------
        A bool indicating if the animal is alive
        """
        if self.energy() > 0 and self.age() < self._population.max_age and self._was_killed == False:
            return True
        else:
            return False
    
    def feed(self):
        """Feed this rabbit with grass from its current patch, if the rabbit is alive. 
        Each unit of grass increases the energy reserve of this rabbit by one.
        The amount of grass a rabbit can eat each turn is limited by its metabolism value multiplied by feeding_metabolism_rate,
        the amount of energy that can be added to its reserve, and the amount of grass available at its current patch 
        """
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
        """ Returns an instance of this class when successful and reduces the energy reserve of this animal 
        by the minimum energy requirement for reproduction multiplied by reproduction_cost_rate.

        Parameters
        ----------
        newborn_patch: An instance of the class Patch, where a potential newborn animal can spawn.

        Return
        -------
        An instance of this class with age zero located at the provided Patch.
        """
        if self.can_reproduce() and self.is_alive():
            probability = self._population.reproduction_probability
            reproduction_res = random.random()
            if reproduction_res <= probability:
                self._energy = self.energy() - self._population.reproduction_min_energy * Rabbit.reproduction_cost_rate
                rabbit = Rabbit(population = self._population,
                                patch = newborn_patch,
                                age = 0)
                # If animal dies after reproduction, remove it
                if self.is_alive() == False:
                    animal = self #This is done to avoid confusion between self referring to the animal or the patch
                    animal.patch().remove(animal)

                return rabbit
        
    def predators_in(self, patch: "Patch") -> bool:
        """ Check if the given patch has an alive fox.
        
        Parameters
        ----------
        - patch: An instance of the class patch

        Return
        ------
        A bool indicating if there is an alive fox at the given patch
        """
        return patch.has_alive_fox()


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
        self._patch_grass = random.randint(0, Patch.max_grass_amount)

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
        """ Checks if there is an alive fox at the patch.

        Returns
        -------
        A bool indicating if there is an alive fox
        """
        for animal in self._animals:
            if isinstance(animal, Fox) and animal.is_alive():
                return True
            else:
                return False

    def has_alive_rabbit(self) -> bool:
        """ Checks if there is an alive rabbit at the patch.

        Returns
        -------
        A bool indicating if there is an alive rabbit
        """
        for animal in self._animals:
            if isinstance(animal, Rabbit) and animal.is_alive():
                return True
            else:
                return False
        
    def add(self, animal: "Animal") -> None:
        """ Add an animal to the patch
        Parameters
        ----------
        - animal: An instance of the class Animal
        """
        self._animals.append(animal)

    def remove(self, animal) -> None:
        """ Remove a given animal from this patch.
        Parameters
        ----------
        - animal: An instance of the class Animal
        """
        self._animals.remove(animal)

    # __str__ is not used, since it defaults to __repr__ if not defined
    def __repr__(self) -> str:
        return ( f"Patch:\n"
                 f"Coordinates = {self.coordinates()}\n "
                 f"Grass_amount = {self._patch_grass}\n "
                 f"Animals = {self._animals}\n ")