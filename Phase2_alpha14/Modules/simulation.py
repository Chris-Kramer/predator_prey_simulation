"""
Authors: @Merete, @Christoffer, @Andreas
"""
import os
import sys
import random
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
    Empty_world: A matrix representing the simulated world.
    
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
    """ Returns a random field from the world and its coordinates.

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
    # Defining foxes and creating lists for their later coordinates
    foxes = params.foxes
    rabbits = params.rabbits   
    coord_foxes = []
    coord_rabbits = []
    
    # Adding the foxes and checking for duplicate coordinates
    for fox in range(0, (foxes.initial_size)):
        field_fox = get_rand_field(world)
        while field_fox.coordinates() in coord_foxes:
            field_fox = get_rand_field(world)    
        fox = ents.Fox(foxes, field_fox, random.randint(0, foxes.max_age))
        coord_foxes.append(field_fox.coordinates())
        
    # Adding the rabbits and checking for duplicate coordinates
    for rabbit in range(0, (rabbits.initial_size)):
        field_rabbit = get_rand_field(world)
        while field_rabbit.coordinates() in coord_rabbits:
            field_rabbit = get_rand_field(world)
        rabbit = ents.Rabbit(rabbits, field_rabbit, random.randint(0, rabbits.max_age))
        coord_rabbits.append(field_rabbit.coordinates())

def _nearest_coords(world, ns_pos, we_pos, movement = "queen"):
    """Get neighbour fields according to specified coordinates
    This function gets all  neighbours from the world according to north south and west east coordinates. 
    If it is less than 0 it will take a coordinate from the opposite side. 
    Neighbour fields can be chosen according to rook, bishop, or queen movement. 

    Precondition
    -------------
    A given coordinate will not exceed the index of the world when + 1 is added to it.

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
    It returns a list of 8 fields that are neighbours.
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
    This function primarily handles indeces and uses a hidden function for getting the correct fields.
    
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
        if ns_pos == len(world) - 1: ns_pos = - 1 # Minus 1 so our index becomes 0 when we say plus 1
        if we_pos == len(world[0]) - 1: we_pos = - 1        
        return _nearest_coords(world, ns_pos, we_pos, movement)

    # Island
    else:
        if ns_pos == 0: ns_pos = 1
        if we_pos == 0: we_pos = 1
        if ns_pos == len(world) - 1: ns_pos = len(world) - 2 #Minus 2 so our index will become len(world) - 1
        if we_pos == len(world[0]) - 1: we_pos = len(world[0]) - 2          
        return _nearest_coords(world, ns_pos, we_pos, movement)
    
    
def reproduce_animal(animal, nearby_fields):
    """ Test if the animal can reproduce according to the geographical and internal rules of reproduction.
    If the animal can reproduce it will activate the animal.reproduce() To a random field.
    Otherwise it wont do anything. It will return a Bool indicating whether it reproduced or not and a newborn or None.

    Parameters
    -----------
    animal: An instance of the class "Animal" from the module "entities".
    nearby_fields: A list of nearby fields

    Return
    ---------
    Bool
    Optional[Animal]
    """
    # List of all mates nearby and fields devoid of predators
    mates = [patch for patch in nearby_fields if animal.same_species_in(patch) and not animal.predators_in(patch)] 
    # List of empty fields nearby
    empty_fields = [patch for patch in nearby_fields if len(patch.animals()) == 0]
    
    #Check if there are mates, empty fields and if the animal can reproduce
    if len(empty_fields) > 0 and len(mates) > 0 and animal.can_reproduce():
        rand_spawn_field = empty_fields[random.randint(0,len(empty_fields)-1)] # Random field for spawning
        newborn = animal.reproduce(rand_spawn_field)
        if newborn is not None: return True, None
    return False, None


def move_animal(animal, nearby_fields):
    """ Move animal to random valid empty field nearby.
    Otherwise do nothing.
    If the animal moves, it will return True, otherwise it will return False

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

def collect_stats(stats, params):
    """ Collect statistics on current simulation step
    
    Parameters
    -----------
    params: An instance of the class "Simulation" from the module "parameters"
    stats: A dictionary contaiing the following key-value pairs:
        - "rabbits": List[Rabbit],
        - "new_born_rabbits": List[Rabbit],
        - "foxes": List[Fox],
        - "new_born_foxes": List[Fox]

    Preconditions
    -------------
    The rabbits in stats["new_born_rabbits] are born in current simulation step
    The foxes in stats["new_born_foxes] are born in current simulation step
    stats[rabbits] contains ALL rabbits (dead or alive) in current simulation step
    stats[foxes] contains ALL foxes (dead or alive) in current simulation step

    Return
    --------
    A dictionary of with relevant statistics on current step, containing the following key-value pairs:
        - "foxes_alive": int, # A count of all alive rabbits
        - "foxes_born": int, # A count of all foxes born
        - "foxes_starved": int, # A count of all foxes that starved to death 
        - "foxes_old": int, # A count of all foxes that died of old age
        - "dead_foxes": List[Foxes], # List of all dead foxes 
        - "energy_foxes": int, # The total energy of all foxes
        - "rabbits_alive": int, # A count of all rabbits alive 
        - "rabbits_born": int, # A count of all rabbits born 
        - "rabbits_starved": int, # A count of all rabbits that starved to death  
        - "rabbits_prey": int, # A count of all rabbits that died of predation
        - "dead_rabbits": List[Rabbit], # List of all dead rabbits  
        - "energy_rabbits": int, # The total energy of all foxes
        - "death_coords": List[List[int]] # A matrix representing the world, conatining the death count of each patch, 
    """
    # Statistics on populations
    stats_pop = {
        #Fox stats
        "foxes_alive": 0,
        "foxes_born": len(stats["new_born_foxes"]),
        "foxes_starved": 0,
        "foxes_old": 0,
        "dead_foxes": [],
        "energy_foxes": 0, 
        # Rabbits
        "rabbits_alive": 0,
        "rabbits_born": len(stats["new_born_rabbits"]),
        "rabbits_starved": 0,
        "rabbits_old": 0,
        "rabbits_prey": 0,
        "dead_rabbits": [],
        "energy_rabbits": 0,
        "death_coords": create_world(params)
        }  
    
    for rabbit in stats["rabbits"]:
        stats_pop["energy_rabbits"] += rabbit.energy() # Energy Stats
        if rabbit.is_alive(): stats_pop["rabbits_alive"] += 1 # Living stats
        else: # Death stats
            stats_pop["dead_rabbits"].append(rabbit.age())
            if rabbit.age() >= params.rabbits.max_age: stats_pop["rabbits_old"] += 1 # Old age
            elif rabbit.energy() <= 0: stats_pop["rabbits_starved"] += 1 # Starvation
            elif rabbit.was_killed():
                stats_pop["rabbits_prey"] += 1
                # Count kills on patch
                ns_pos = rabbit.patch().coordinates()[0]
                we_pos = rabbit.patch().coordinates()[1]
                stats_pop["death_coords"][ns_pos - 1][we_pos - 1] += 1
                
    
    for fox in stats["foxes"]:
        stats_pop["energy_foxes"] += fox.energy() # Energy Stats
        if fox.is_alive(): stats_pop["foxes_alive"] += 1 # Living stats
        else: # Death stats
            stats_pop["dead_foxes"].append(fox.age())
            if fox.age() >= params.foxes.max_age: stats_pop["foxes_old"] += 1 # Old age
            elif fox.energy() <= 0: stats_pop["foxes_starved"] += 1 # Starvation

    return stats_pop


def update_entities(world, params, movement):
    """ This function updates each entity in the world

    Parameters
    ----------
    world: A matrix representing the simulated world containing patches in every field.
    params: An instance of the class "Simulation" from the module "parameters"
    movement: Movement that defines neighbours can be either
        - Queen (Default): "queen" or "q"
        - Rook: "rook" or "r"
        - Bishop: "bishop" or "b"   

    Return
    ---------
    Returns a dictionary containing the following key-value pairs:
        - "rabbits": List[Rabbit], # A list of every rabbit in the current simulation step
        - "new_born_rabbits": List[Rabbit], # A list of every newborn rabbit in the current simulation step
        - "foxes": List[Fox], # A list of every fox in the current simulation step
        - "new_born_foxes": List[Fox] # A list of every newborn fox in the current simulation step  
    """
    stats = {
        "rabbits": [],
        "new_born_rabbits": [],
        "foxes": [],
        "new_born_foxes": []
    }
    ns_pos = 0 # North South position
    for row in world:
        we_pos = 0
        for patch in row:
            kills = 0
            patch.tick()
            for animal in patch.animals():          
                #Append animals
                if isinstance(animal, ents.Fox) and animal not in stats["foxes"] : stats["foxes"].append(animal)
                elif isinstance(animal, ents.Rabbit) and animal not in stats["rabbits"]: stats["rabbits"].append(animal)
                #Simulation
                animal.tick()
                animal.feed()
                #Reproduce or move
                near_reproduction = get_near_by_fields(animal, world, params, movement = "q") 
                reproduction, newborn = reproduce_animal(animal, near_reproduction)
                if reproduction and newborn is not None:
                    if isinstance(newborn, ents.Fox): stats["new_born_foxes"].append(newborn) 
                    else: stats["new_born_rabbits"].append(newborn)
                elif not reproduction and animal.is_alive():
                    nearby_movement = get_near_by_fields(animal, world, params, movement)
                    move_animal(animal, nearby_movement)
            we_pos += 1
        ns_pos += 1

    return stats


def run(params):
    """Runs the simulation according to the specified parameters.

    Parameters
    ----------
    params: params: An instance of the class "Simulation" from the module "parameters"

    Return
    ----------
    An instance of the class SimulationStats from the module "results".
    """
    #Initialize world
    world = create_world(params)
    fill_world(world)
    populate_world(params, world)
    # Configure movement type
    choice = input("Chose movement style\n['r' or 'rook' for rook; 'b' or 'bishop' for bishop; default style = Queen] ")
    if choice == "r" or choice == "rook": movement = choice
    elif choice == "b" or choice == "bishop": movement = choice
    else: movement = "q"
    
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
    # Rabbit stats
    r_pop_stats = res.PopulationStats()
    r_pop_stats.age_at_death = []  
    r_pop_stats.avg_energy_per_step = [] 
    r_pop_stats.dead_by_old_age = 0  
    r_pop_stats.dead_by_predation = 0 
    r_pop_stats.dead_by_starvation  = 0 
    r_pop_stats.size_per_step = [] 
    r_pop_stats.total = params.rabbits.initial_size
    
    # Foxes stats
    f_pop_stats = res.PopulationStats()
    f_pop_stats.age_at_death = [] 
    f_pop_stats.avg_energy_per_step = [] 
    f_pop_stats.dead_by_old_age = 0 
    f_pop_stats.dead_by_predation = 0  
    f_pop_stats.dead_by_starvation  = 0
    f_pop_stats.size_per_step = []
    f_pop_stats.total = params.foxes.initial_size 
    
    #Simulation stats
    sim_stats = res.SimulationStats()
    sim_stats.avg_energy_per_step = []
    sim_stats.foxes = f_pop_stats
    sim_stats.kills_per_patch = create_world(params)
    sim_stats.rabbits = r_pop_stats
    sim_stats.steps = 0

    # Run simulation
    vis.start()
    for i in range(params.execution.max_steps):
        vis.update(i)
        stats = collect_stats(update_entities(world, params, movement), params)
        # Count Rabbit stats
        r_pop_stats.total += stats["rabbits_born"]
        r_pop_stats.size_per_step.append(stats["rabbits_alive"])
        r_pop_stats.dead_by_starvation += stats["rabbits_starved"]
        r_pop_stats.dead_by_predation += stats["rabbits_prey"]
        r_pop_stats.dead_by_old_age += stats["rabbits_old"]
        for r_age in stats["dead_rabbits"]: r_pop_stats.age_at_death.append(r_age) # Age of death
        r_avg_energy = stats["energy_rabbits"] / r_pop_stats.total
        r_pop_stats.avg_energy_per_step.append(r_avg_energy)
        # Count Foxes stats
        f_pop_stats.total += stats["foxes_born"]
        f_pop_stats.size_per_step.append(stats["foxes_alive"])
        f_pop_stats.dead_by_starvation += stats["foxes_starved"]
        f_pop_stats.dead_by_predation = 0 # Foxes wont be killed by a rabbit.
        f_pop_stats.dead_by_old_age += stats["foxes_old"]
        for f_age in stats["dead_foxes"]: f_pop_stats.age_at_death.append(r_age)
        f_avg_energy = stats["energy_foxes"] / f_pop_stats.total
        f_pop_stats.avg_energy_per_step.append(f_avg_energy)

        # Count simulation stats
        sim_stats.avg_energy_per_step.append(f_avg_energy + r_avg_energy) # Avg. energy for both foxes and rabbits
        sim_stats.steps = i + 1 
        # Kills per patch
        ns_pos = 0 #North South
        for row in sim_stats.kills_per_patch:
            we_pos = 0 # West East
            for patch in row:
                sim_stats.kills_per_patch[ns_pos][we_pos] += stats["death_coords"][ns_pos][we_pos]
                we_pos +=1
            ns_pos += 1

    vis.stop()
    return sim_stats

if __name__ == '__main__':
    pass
    
