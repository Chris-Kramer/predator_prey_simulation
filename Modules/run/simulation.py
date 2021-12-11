"""
Authors: @Merete, @Christoffer, @Andreas
"""
import os
import sys
import random

sys.path.append(os.path.join("..", "classes"))
import parameters, visualiser, results as res, entities as ents


# Creating an empty world using parameters for 
def create_world(params):
    """Create an empty world for entities to later be filled in.
    
    Parameters
    ----------
    params: An instance of the class "Simulation" from the module "parameters"
    
    Return
    --------
    A list with nested lists corresponding to a grid with the dimensions of the world.
    """
    field = 0 # Zero for empty field 
    nsl = params.world.north_south_length
    wel = params.world.west_east_length
    return [[field for col in range(wel)] for row in range(nsl)]


# Filling the empty world with patches
def fill_world(empty_world):
    """Fill an empty world with Patches
    
    Parameters
    ----------
    empty_world: A matrix representing the simulated world.
    
    Return
    ---------
    No return value
    """
    ns_pos = 0 #North-South position
    for row in empty_world:
        we_pos = 0 #West-East position
        for field in row:
            empty_world[ns_pos][we_pos] = ents.Patch(ns_pos, we_pos)
            we_pos += 1     
        ns_pos +=1

        
# Get random field in world
def get_rand_field(world):
    """Returns a random field from the world and its coordinates.

    Parameters
    ----------
    world: A matrix representing the simulated world.

    Return
    ---------
    A random position from the provided world
    """  
    nsl = len(world)
    wel = len(world[0])
    random_wel = random.randint(0, wel - 1) # minus 1 due to zero indexing
    random_nsl = random.randint(0, nsl - 1)
    return world[random_nsl][random_wel]


# Filling the patches with entities
def populate_world(params, world):
    """Function to populate an empty world with patches

    Parameters
    ------------
    params: An instance of the class "Simulation" from the module "parameters"
    world: A matrix representing the simulated world filled with patch entities.

    Return
    ----------
    No return value 
    """
    # Helper function for creating new animals
    def _create_animals(population, world):
        coords_animals = []
        for animal in range(population.initial_size):
            # Get empty coordinate for animal
            field_animal = get_rand_field(world)
            while field_animal.coordinates() in coords_animals:
                field_animal = get_rand_field(world)        
            # Create animal depending on population
            if population.species == "foxes":
                fox = ents.Fox(population, field_animal, random.randint(0, population.max_age))
            else: 
                rabbit = ents.Rabbit(population, field_animal, random.randint(0, population.max_age))
            coords_animals.append(field_animal.coordinates())
      
    foxes = params.foxes
    _create_animals(foxes, world)
    rabbits = params.rabbits
    _create_animals(rabbits, world)

def _nearest_coords(world, ns_pos, we_pos, movement = "queen"):
    """Get neighbour fields according to specified coordinates
    This function gets all  neighbours from the world according to north south and west east coordinates.  
    Neighbour fields can be chosen according to rook, bishop, or queen movement. 

    Precondition
    -------------
    A given coordinate will not exceed the index of the world when + 1 is added to it.
    A given coordinate follows zero-indexing.
    
    Parameters
    -------------
    world: A matrix representing the simulated world
    ns_pos: The north south position
    we_pos: The west east position
    movement: Movement that defines neighbours can be either
        - Queen (Default): "queen" or "q"
        - Rook: "rook" or "r"
        - Bishop: "bishop" or "b"
    
    Return
    ------------
    A list of patches which are neighbouring fields
    """
    # Fields north of current position
    north_left = world[ns_pos - 1][we_pos - 1]
    north_middle = world[ns_pos - 1][we_pos]
    north_right = world[ns_pos - 1][we_pos + 1]  
    # Fields on same north-south position as the current position
    same_left = world[ns_pos][we_pos - 1]
    same_right = world[ns_pos][we_pos + 1]
    # Fields South of current position
    south_left = world[ns_pos + 1][we_pos - 1]
    south_middle = world[ns_pos + 1][we_pos]
    south_right = world[ns_pos + 1][we_pos + 1]

    # Rook movement
    if movement.lower() == "rook" or movement.lower() == "r":
        near_fields = [north_middle, same_left, same_right, south_middle]      
    # Queen movement
    elif movement.lower() == "queen" or movement.lower() == "q":
        near_fields = [north_left, north_middle, north_right,
                       same_left, same_right,
                       south_left, south_middle, south_right]
    # Bishop movement
    elif movement.lower() == "bishop" or movement.lower() == "b":
        near_fields = [north_left, north_right, south_left, south_right]

    return near_fields

def get_near_by_fields(animal, world, params, movement = "q"):
    """ Get nearby fields of an animal according to specified movement neighbours.
    This function primarily handles indeces and uses a semi-private function for getting the correct fields.
    
    Parameters
    -----------
    params: An instance of the class "Simulation" from the module "parameters"
    world: A matrix representing the simulated world filled with patch entities
    animal: An instance of the class "Animal" from the module "entities".
    movement: Movement that defines neighbours can be either
        - Queen (Default): "queen" or "q"
        - Rook: "rook" or "r"
        - Bishop: "bishop" or "b"
 
    Return
    ---------
    Returns a list of fields from the given world. 
    """
    coordinates = animal.patch().coordinates()
    ns_pos = coordinates[0] # North South Position
    we_pos = coordinates[1] # West East Position

    # Toroid
    if params.world.is_toroid:
        if ns_pos == len(world) - 1:
            ns_pos = - 1 # Minus 1 so our index becomes 0 when we say plus 1
        if we_pos == len(world[0]) - 1:
            we_pos = - 1        
        return _nearest_coords(world, ns_pos, we_pos, movement)
    # Island
    else:
        
        if ns_pos == 0:
            ns_pos = 1
        if we_pos == 0:
            we_pos = 1
        if ns_pos == len(world) - 1:
            ns_pos = len(world) - 2 # Minus 2 so our index will become len(world) - 1
        if we_pos == len(world[0]) - 1:
            we_pos = len(world[0]) - 2          
        return _nearest_coords(world, ns_pos, we_pos, movement)
    
    
def reproduce_animal(animal, nearby_fields):
    """ Test if the animal can reproduce according to the geographical and internal rules of reproduction.
    If the animal can reproduce it will activate the animal.reproduce() To a random field.
    Otherwise it wont do anything. It will return a Bool indicating whether it reproduced or not and a newborn or None.

    Parameters
    -----------
    animal: An instance of the class "Animal" from the module "entities".
    nearby_fields: A list of neighbouring fields

    Return
    ---------
    Boolean indicating if reproduction was succesful
    The newborn animal or None depending on the outcome of reproduction 
    """
    # List of all mates nearby and fields devoid of predators
    mates = [patch for patch in nearby_fields if animal.same_species_in(patch) and not animal.predators_in(patch)] 
    # List of empty fields nearby
    empty_fields = [patch for patch in nearby_fields if len(patch.animals()) == 0]
    
    #Check if there are mates, empty fields and if the animal can reproduce
    if len(empty_fields) > 0 and len(mates) > 0 and animal.can_reproduce():
        rand_spawn_field = empty_fields[random.randint(0,len(empty_fields)-1)] # Random field for spawning
        newborn = animal.reproduce(rand_spawn_field)
        if newborn is not None:
            return True, newborn
    return False, None # This will only execute if the above if-statements evaluates to False


def move_animal(animal, nearby_fields):
    """Move animal to random valid empty field nearby if it is possible

    Parameters
    -----------
    animal: An instance of the class "Animal" from the module "entities".
    nearby_fields: A list of nearby fields

    Return
    ---------
    No return value   
    """
    # List of fields without same species
    empty_fields = [patch for patch in nearby_fields if not animal.same_species_in(patch)]

    if len(empty_fields) > 0:
        rand_empty_field = empty_fields[random.randint(0,len(empty_fields)-1)] # Random field for spawning
        animal.move_to(rand_empty_field)

        
def _collect_stats(animals, newborns, population, pop_stats, sim_stats):
    """ This function collects statistics and updates the relevant classes

    Parameters
    ----------
    animals: A list of animals
    newborns: A list of newborns animals
    population: An instance of the class "Population" from the module "parameters"
    pop_stats: An instance of the class "PopulationStats" from the module "results"
    sim_stats: An instance of the class "SimulationStats" from the module "results"

    Preconditions
    -------------
    animals is a list of animals of the same species
    newborns and animals contain animals of the same species
    population is the same species as animals and newborns
    pop_stats is only used to track animals of the same species as animals and newborn

    Return
    -------
    No return value
    """
    
    # Update total size of population
    pop_stats.total += len(newborns)

    # Count stats
    total_energy = 0 #Used for calculating average energy
    alive_animals = 0
    for animal in animals:
        total_energy += animal.energy()
        # Alive animals
        if animal.is_alive():
            alive_animals += 1
        # Dead animals
        else:
            pop_stats.age_at_death.append(animal.age())
            # Old age
            if animal.age() >= population.max_age:
                pop_stats.dead_by_old_age += 1
            # Starvation
            elif animal.energy() <= 0:
                pop_stats.dead_by_starvation += 1
            # Predation and kills on patch
            elif isinstance(animal, ents.Rabbit) and animal.was_killed():
                pop_stats.dead_by_predation += 1 
                ns_pos = animal.patch().coordinates()[0]# North South Position
                we_pos = animal.patch().coordinates()[1]# West East Position
                sim_stats.kills_per_patch[ns_pos - 1][we_pos - 1] += 1

    # Update class attributes that expects lists as values
    pop_stats.size_per_step.append(alive_animals)
    try:
        pop_stats.avg_energy_per_step.append(total_energy/len(animals)) 
    except ZeroDivisionError:
        pop_stats.avg_energy_per_step.append(0)


def update_entities(world, params,
                    r_pop_stats, f_pop_stats,
                    sim_stats, movement):   
    """ This function updates each entity in the world and collects relevant statistics

    Parameters
    ----------
    world: A matrix representing the simulated world containing patches in every field
    params: An instance of the class "Simulation" from the module "parameters"
    r_pop_stats: An instance of the class "PopulationStats" from the module "results" for rabbits
    f_pop_stats: An instance of the class "PopulationStats" from the module "results" for foxes
    movement: Movement that defines neighbours can be either
        - Queen (Default): "queen" or "q"
        - Rook: "rook" or "r"
        - Bishop: "bishop" or "b"   

    Return
    ---------
    No return value
    """

    rabbits = []
    newborn_rabbits = []
    foxes = []
    newborn_foxes = []
    for row in world:
        for patch in row:
            kills = 0
            patch.tick()
            for animal in patch.animals():          
                #Append animals
                if isinstance(animal, ents.Fox) and animal not in foxes:
                    foxes.append(animal)
                elif isinstance(animal, ents.Rabbit) and animal not in rabbits:
                    rabbits.append(animal)
                
                #Simulation
                animal.tick()
                animal.feed()
                #Reproduce
                near_reproduction = get_near_by_fields(animal, world, params, movement = "q") 
                reproduction, newborn = reproduce_animal(animal, near_reproduction)
                if reproduction and isinstance(newborn, ents.Fox): #If fox
                    newborn_foxes.append(newborn)
                elif reproduction: #If rabbit
                    newborn_rabbits.append(newborn)
                # Move
                if not reproduction and animal.is_alive():
                    nearby_movement = get_near_by_fields(animal, world, params, movement)
                    move_animal(animal, nearby_movement)

    # Collect stats on each population
    # Rabbits
    _collect_stats(animals = rabbits,
                   newborns = newborn_rabbits,
                   population = params.rabbits,
                   pop_stats = r_pop_stats,
                   sim_stats = sim_stats)
    # Foxes
    _collect_stats(animals = foxes,
                   newborns = newborn_foxes, 
                   population = params.foxes,
                   pop_stats = f_pop_stats,
                   sim_stats = sim_stats)

def run(params):
    """Runs the simulation according to the specified parameters collects statistics

    Parameters
    ----------
    params: params: An instance of the class "Simulation" from the module "parameters"

    Return
    ----------
    An instance of the class "SimulationStats" from the module "results".
    """
    #Initialize world
    world = create_world(params)
    fill_world(world)
    populate_world(params, world)
    
    # Configure movement type
    choice = input("Chose movement style\n['r' or 'rook' for rook; 'b' or 'bishop' for bishop; default style = Queen] ")
    if choice == "r" or choice == "rook":
        movement = choice
    elif choice == "b" or choice == "bishop":
        movement = choice
    else:
        movement = "q"
    
    #Create and configure visualiser
    flat_world = [patch for col in world for patch in col] # Visualíser only works with a flat list
    if params.execution.batch:
        vis = visualiser.Batch(total_steps = params.execution.max_steps)
    else:
        choice = input("Visualize in colour or grayscale?\n['colour' or 'c' for colourgraphics; default scale = Grayscale] ")
        if choice == "c" or choice == "colour":
            vis = visualiser.ColourGraphics(total_steps = params.execution.max_steps,
                                            patches = flat_world,
                                            width = len(world),
                                            height =len(world[0]),
                                            delay = params.execution.step_delay,
                                            grass_levels = True)
        else:
            vis = visualiser.GrayscaleGraphics(total_steps = params.execution.max_steps,
                                            patches = flat_world,
                                            width = len(world),
                                            height =len(world[0]),
                                            delay = params.execution.step_delay,
                                            grass_levels = True)
    # Initialize object for rabbit stats
    r_pop_stats = res.PopulationStats()
    r_pop_stats.age_at_death = []  
    r_pop_stats.avg_energy_per_step = [] 
    r_pop_stats.dead_by_old_age = 0  
    r_pop_stats.dead_by_predation = 0 
    r_pop_stats.dead_by_starvation  = 0 
    r_pop_stats.size_per_step = [] 
    r_pop_stats.total = params.rabbits.initial_size
    
    # Initialize object for Foxes stats
    f_pop_stats = res.PopulationStats()
    f_pop_stats.age_at_death = [] 
    f_pop_stats.avg_energy_per_step = [] 
    f_pop_stats.dead_by_old_age = 0 
    f_pop_stats.dead_by_predation = 0  
    f_pop_stats.dead_by_starvation  = 0
    f_pop_stats.size_per_step = []
    f_pop_stats.total = params.foxes.initial_size 
    
    # Initialize object for Simulation stats
    sim_stats = res.SimulationStats()
    sim_stats.foxes = f_pop_stats
    sim_stats.kills_per_patch = create_world(params)
    sim_stats.rabbits = r_pop_stats
    sim_stats.steps = params.execution.max_steps
    
    # Run simulation
    vis.start()
    for i in range(params.execution.max_steps):
        vis.update(i)
        update_entities(world, params,
                        r_pop_stats, f_pop_stats,
                        sim_stats, movement)
    vis.stop()

    # Calculate and save total average energy from both populations
    sim_stats.avg_energy_per_step = [f_pop_stats.avg_energy_per_step[i] + r_pop_stats.avg_energy_per_step[i]
                                     for i in range(params.execution.max_steps)]
    return sim_stats

if __name__ == '__main__':
    pass
    
