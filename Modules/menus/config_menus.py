import advanced_menu as am
import sys
import os

sys.path.append(os.path.join("..", "classes"))
import parameters


#---------- Sub-menu: configure world ----------
def configure_world(sim_parameters):
    """Configure world parameters. 
    This function displays the menu for configuring the world parameter and changes their values based on user input.

    Parameters
    -----------
    - sim_parameters: An instance of the class "Simulation" from the module "parameters".

    Return 
    -----------
    No return value

    Example
    -----------
    >>> import parameters
    >>> params = parameters.Simulation()
    >>> configure_world(params)
    Choose parameter to configure:
        [1] Shape
        [2] North-South length
        [3] West-East length
        [0] Go back
    Enter parameter:  
    """
    world = sim_parameters.world
    sizes_foxes = sim_parameters.foxes.initial_size # For preconditions testing
    sizes_rabbits = sim_parameters.rabbits.initial_size # For preconditions testing
    # Choice prompt
    print("Choose parameter to configure:"  +
          "\n\t[1] Shape" +
          "\n\t[2] North-South length" +
          "\n\t[3] West-East length" +
          "\n\t[0] Go back")
    choice = input("Enter parameter: ")
    # set shape
    if choice == "1":
        select_shape(sim_parameters)           
    # set North-South length
    elif choice == "2":
        try:
            north_south = int(input("Enter North-South lenght of the world: "))
            world_size =  north_south * world.west_east_length
            if (0 < north_south and
                world_size > sizes_foxes and
                world_size > sizes_rabbits):
                world.north_south_length = north_south
                print("North-South set to " + str(north_south))
                configure_world(sim_parameters)
            else:
                print("Invalid input. North-South must be a positive integer and larger than population size")
                configure_world(sim_parameters)
        except ValueError:
            print("Invalid input. North-South length must be an integer")
            configure_world(sim_parameters)             
    # set West-East length
    elif choice == "3":
        try:
            west_east = int(input("Enter West-East lenght of the world: "))
            world_size = west_east * world.north_south_length
            if (0 < west_east and
                world_size > sizes_foxes and
                world_size > sizes_rabbits):
                world.west_east_length = west_east
                print("West-East length set to " + str(west_east))
                configure_world(sim_parameters)
            else:
                print("Invalid input. West-East must be a positive integer and larger than population size")
                configure_world(sim_parameters)
            
            
        except ValueError:
            print("Invalid input. West-East length must be an integer")
            configure_world(sim_parameters)                  
    # Back to top menu
    elif choice == "0":
        am.advanced_menu(sim_parameters)
    # Invalid input
    else:
        print("Invalid choice...")
        configure_world(sim_parameters)

        
# ------ Sub-sub-menu: select shape ------
def select_shape(sim_parameters):
    """Configure shape
    This function displays a menu which lets the user choose the shape of the world (toroid or island).

    Parameters
    ------------
    - sim_parameters: An instance of the class "Simulation" from the module "parameters".

    Return
    -----------
    No return values.

    Example
    -----------
    >>> import parameters
    >>> params = parameters.Simulation()
    >>> select_shape(params)
    Choose shape: 
        [1] Toroid 
        [2] Island 
        [0] Go back
    Enter selection: 
    """
    world = sim_parameters.world
    # Choice prompt
    print("Choose shape:"
          "\n\t[1] Toroid" +
          "\n\t[2] Island" +
          "\n\t[0] Go back")
    choice = input("Enter selection: ")
    # Toroid
    if choice == "1":
        world.is_toroid = True
        print("World shape set to Toroid")
        configure_world(sim_parameters)
    # Island
    elif choice == "2":
        world.is_toroid = False
        print("World shape set to Island")
        configure_world(sim_parameters)
    # Go back
    elif choice == "0":
        configure_world(sim_parameters)
    # Invalid input
    else:
        print("Invalid choice")
        select_shape(sim_parameters)

        
#---------- Submenu: configure species ----------
def configure_species(sim_parameters, species):
    """Configure species
    This function displays a menu, which lets the user configure the parameters of a given population species in the simulation.

    Parameters
    -----------
    - sim_parameters: An instance of the class "Simulation" from the module "parameters".
    - species: The attribute "foxes" or "rabbits" associated with the class "Simulation" from the module "parameters".

    Return
    ----------
    No return values.
    
    Example
    ----------
    >>> import parameters
    >>> params = parameters.Simulation()
    >>> rabbits = params.rabbits
    >>> configure_species(params, rabbits)
    Choose parameter to configure: 
        [1] Initial size  
        [2] Metabolism 
        [3] Maximum energy 
        [4] Maximum age 
        [5] Reproduction probability 
        [6] Reproduction energy 
        [7] Reproduction age 
        [0] Go back
    Enter parameter:   
    """   
    # Choice prompt
    print("Choose parameter to configure:" +
          "\n\t[1] Initial size" +
          "\n\t[2] Metabolism" +
          "\n\t[3] Maximum energy" +
          "\n\t[4] Maximum age" + 
          "\n\t[5] Reproduction probability" +
          "\n\t[6] Reproduction energy" + 
          "\n\t[7] Reproduction age" + 
          "\n\t[0] Go back")
    choice = input("Enter parameter: ")
    # Initial size
    if choice == "1":
        try:
            initial_size = int(input("Enter initial size: "))
            world = sim_parameters.world
            world_size = world.north_south_length * world.west_east_length
            if 0 < initial_size < world_size:
                species.initial_size = initial_size
                print("Initial size set to " + str(initial_size))
                configure_species(sim_parameters, species)
            else:
                print("Invalid input. The size of a species must be larger than 0 and less than the size of the world")
                configure_species(sim_parameters, species)
        except ValueError:
            print("Invalid input. Input must be an integer")
            configure_species(sim_parameters, species)
    # Metabolism
    elif choice == "2":
        try:
            metabolism = int(input("Enter metabolism: "))
            if 0 <= metabolism: 
                species.metabolism = metabolism
                print("Metabolism set to " + str(metabolism))
                configure_species(sim_parameters, species)
            else:
                print("Invalid input. Metabolism must be non-negative")
                configure_species(sim_parameters, species)
        except ValueError:
            print("Invalid input. Input must be an integer")
            configure_species(sim_parameters, species)
    # Max energy
    elif choice == "3":
        try:
            max_energy = int(input("Enter max energy: "))
            if 0 < max_energy:
                species.max_energy = max_energy
                print("Max energy set to " + str(max_energy))
                configure_species(sim_parameters, species)
            else:
                print("Invalid input. Max energy must be a positive integer")
                configure_species(sim_parameters, species)
        except ValueError:
            print("Invalid input. Max energy must be a positive integer")
            configure_species(sim_parameters, species)              
    # Max age
    elif choice == "4":
        try:
            max_age = int(input("Enter max age: "))
            if 0 < max_age:
                species.max_age = max_age
                print("Max age set to " + str(max_age))
                configure_species(sim_parameters, species)
            else:
                print("Invalid input. max_age must be a positive integer")
                configure_species(sim_parameters, species)
        except ValueError:
            print("Invalid input. Input must be a positive integer")
            configure_species(sim_parameters, species)               
    # Reproduction probability    
    elif choice == "5":
        try:
            reproduction_probability = float(input("Enter reproduction probability: "))
            if 0 <= reproduction_probability <= 1: # Precondition not specified in documentation. But negative probability makes no sense
                species.reproduction_probability = reproduction_probability
                print("Reproduction probability set to " + str(reproduction_probability))
                configure_species(sim_parameters, species)
            else:
                print("Invalid input. Input must be a non-negative floating point between 0 and 1")
                configure_species(sim_parameters, species)
        except ValueError:
            print("Invalid input. Input must be a floating point value")
            configure_species(sim_parameters, species)                
    # Reproduction minimum energy    
    elif choice == "6":
        try:
            reproduction_min_energy = int(input("Enter minimum energy for reproduction: "))
            if 0 <= reproduction_min_energy: # Precondition not specified in documentation. But negative energy makes no sense
                species.reproduction_min_energy = reproduction_min_energy
                print("Reproduction probability set to " + str(reproduction_min_energy))
                configure_species(sim_parameters, species)
            else:
                print("Invalid input. Input must be a non-negative integer")
                configure_species(sim_parameters, species)                    
        except ValueError:
            print("Invalid input. Input must be an integer")
            configure_species(sim_parameters, species)            
    # Reproduction minimum age
    elif choice == "7":
        try:
            reproduction_min_age = int(input("Enter minimum age for reproduction: "))
            if 0 <= reproduction_min_age:# Precondition not specified in documentation. But negative age makes no sense
                species.reproduction_min_age = reproduction_min_age
                print("Reproduction minimum age set to " + str(reproduction_min_age))
                configure_species(sim_parameters, species)
            else:
                print("Invalid input. Input must be a positive integer")
                configure_species(sim_parameters, species)  
        except ValueError:
            print("Invalid input. Input must be a positive integer")
            configure_species(sim_parameters, species)             
    # Back to top menu
    elif choice == "0":
        am.advanced_menu(sim_parameters)            
    # Invalid input
    else:
        print("Invalid choice...")
        configure_species(sim_parameters, species)


#---------- Sub-menu: configure execution ----------
def configure_execution(sim_parameters):
    """Configure execution
    This function displays a menu, which lets the user configure the execution parameters.

    Parameters
    ------------
    - sim_parameters: An instance of the class "Simulation" from the module "parameters".

    Return
    ------------
    No return value

    Example
    -----------
    >>> import parameters
    >>> params = parameters.Simulation()
    >>> configure_execution(params)
    Choose parameter to configure: 
        [1] Maximum number of steps
        [2] Step delay
        [2] Execution mode 
        [0] Go back
    Enter parameter:  
    """
    execution = sim_parameters.execution
    # Choice prompt
    print("Choose parameter to configure:" +
          "\n\t[1] Maximum number of steps" +
          "\n\t[2] Step delay" +
          "\n\t[3] Execution mode" +
          "\n\t[0] Go back")
    choice = input("Enter parameter: ")       
    # set max steps
    if choice == "1":
        try:
            max_steps = int(input("Enter maximum number of steps: "))
            if 0 < max_steps: # Precondition not specified in documentation, however it seems absurd to accept negative values and 0
                execution.max_steps = max_steps
                print("Max steps set to " + str(max_steps))
                configure_execution(sim_parameters)
            else:
                print("Invalid input. Max steps must be a positive integer")
                configure_execution(sim_parameters)
        except ValueError:
            print("Invalid input. Max steps must be a positive integer")
            configure_execution(sim_parameters)
    # set step delay
    elif choice == "2":
        try:
            step_delay = float(input("Enter step delay: "))
            if 0 <= step_delay: # Precondition is not specified in documentation, however it seems absurd to accept negative values
                execution.step_delay = float(step_delay)
                print("Step delay set to " + str(step_delay))
                configure_execution(sim_parameters)
            else:
                print("Invalid input Step delay must be a positive float or integer")
                configure_execution(sim_parameters)                    
        except ValueError:
            print("Invalid input. Step delay must be a positive float or integer")
            configure_execution(sim_parameters)
    # set mode 
    elif choice == "3":
        select_mode(sim_parameters)
    # Back to top menu
    elif choice == "0":
        am.advanced_menu(sim_parameters)
    # Invalid input
    else:
        print("Invalid choice ...")
        configure_execution(sim_parameters)

        
#----- Sub-sub-menu: select mode ------
def select_mode(sim_parameters):
    """Configure simulation mode
    This function displays a menu, which lets the user select how the simulation is executed (batch or visual).

    Parameters
    ------------
    - sim_parameters: An instance of the class "Simulation" from the module "parameters".

    Return
    -----------
    No return value.
    
    Example
    -----------
    >>> import parameters
    >>> params = parameters.Simulation()
    >>> select_mode(params)
    Choose execution mode: 
        [1] Batch 
        [2] Visual 
        [0] Go back
    Enter simulation mode: 
    """
    execution = sim_parameters.execution
    # Choice prompt
    print("Choose execution mode:" +
          "\n\t[1] Batch" +
          "\n\t[2] Visual" +
          "\n\t[3] Go back")
    modality_choice = input("Enter simulation mode: ")
    # Batch
    if modality_choice == "1":
        execution.batch = True
        print("Mode set to batch")
        configure_execution(sim_parameters)          
    # Visual
    elif modality_choice == "2":
        execution.batch = False
        print("Mode set to visual")
        configure_execution(sim_parameters)
    # Go back
    elif modality_choice == "0":
        configure_execution(sim_parameters)
    # Invalid input
    else:
        print("invalid input")
        select_mode(sim_parameters)

if __name__ == "__main__":
    pass
