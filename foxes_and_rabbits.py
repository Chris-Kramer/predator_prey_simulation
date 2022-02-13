import os
import sys
import time
import typing

# Look for modules in other folders 
sys.path.append(os.path.join("Modules", "classes"))
sys.path.append(os.path.join("Modules", "menus"))
sys.path.append(os.path.join("Modules", "run"))

# Importing the required modules for the script:
import parameters, simulation, reporting, reporting_menu as rm, advanced_menu as am, config_menus as cm

# Visual introduction to the simulation app.
def ascii_text():
    """
    Foxes_and_Rabbits Ascii-text.
    
    When the script is started the ascii-text function is run to display introduction text.
    
    Parameters
    ----------
    - No parameters for this function.
    
    Return
    ------
    - No Return value.
    
    """
    
    print("""
  ___                              _   ___      _    _    _ _      
 | __|____ _____ ___  __ _ _ _  __| | | _ \__ _| |__| |__(_) |_ ___
 | _/ _ \ \ / -_)_-< / _` | ' \/ _` | |   / _` | '_ \ '_ \ |  _(_-<
 |_|\___/_\_\___/__/____,_|_||_\__,_|___|_\__,_|_.__/_.__/_|\__/__/
 
    """)


# Defining a function to display simulation parameters
def display_parameters(params: parameters.Simulation) -> None:
    """
    Display Parameters Function.
    
    Prints (displays) the current parameters that will be used to run the simulation.
    
    Parameters
    ----------
    - "params": An instance of the class "Simulation" from the module "parameters"
    
    Return
    ------
    No Return value.
    
    """
    
    print(f'''
Current Parameters:
------------------- \n
World: {params.world} \n
{params.foxes} \n
{params.rabbits} \n
Execution Method: {params.execution} \n''')


# Defining the quick setup menu:
def quick_setup(params: parameters.Simulation) -> None:
    """
    Quick-Setup Function (menu).
    
    Enables the user to change some parameters of the simulation model instead of all.
    
    When user is done configuring, user is sent back to the configuration menu.
    
    Parameters
    ----------
    - "params": An instance of the class "Simulation" from the module "parameters"
    
    Return
    ------
    No Return value.
    
    """
    
    print('''
    Quick Setup:
    [1] Size of world
    [2] Size of each population
    [3] Maximum number of simulation steps
    [4] Simulation modality
    [0] Done/Go back
    ''')
    choice = input('What would you like to setup?: ')
    
    
    # Size of world
    if choice == "1":
        try:
            world = params.world
            nsl = int(input('Enter a North-South length for the world: '))
            wel = int(input('Enter a West-East length for the world: '))
            world_size = nsl*wel
            rabbits_size = params.rabbits.initial_size
            foxes_size = params.foxes.initial_size
            if 0 < nsl and 0 < wel and world_size > rabbits_size and world_size > foxes_size:
                world.north_south_length = nsl
                world.west_east_length = wel
                quick_setup(params)
            else:
                print("Invalid input: North-South and West-East length must be a positive integer and larger than population size")
                quick_setup(params)
            quick_setup(params)
        
        except ValueError:
            print('Not a valid world size..')
            quick_setup(params)
            
            
    # Size of population
    elif choice == "2":
        try:
            world = params.world
            foxes = params.foxes
            rabbits = params.rabbits
            size_foxes = int(input('Enter a size of the Foxes population: '))
            size_rabbits = int(input('Enter a size of the Rabbits population: '))
            world_size = world.north_south_length * world.west_east_length
            
            if 0 < size_foxes < world_size and 0 < size_rabbits < world_size:
                foxes.initial_size = size_foxes
                rabbits.initial_size = size_rabbits
                quick_setup(params)
            else:
                print("Invalid input. The size of a species must be larger than 0 and less than the size of the world")
                quick_setup(params)
                
        except ValueError:
            print('Not a valid input..')
            quick_setup(params)
            
            
    # Max number of simulation steps
    elif choice == "3":
        try:
            execution = params.execution
            new_max_steps = int(input(f'Enter number of max steps: '))
            if 0 < new_max_steps: 
                execution.max_steps = new_max_steps
                quick_setup(params)
            else:
                print("Invalid input. Max steps must be a positive integer")
                quick_setup(params)
                
        except ValueError:
            print('Not a valid input..')
            quick_setup(params)
             
             
    # Simulation modality  
    elif choice == "4":
        try:
            print('''
            [1] Batch
            [2] Visual
            ''')
            modality = int(input('Pick a modality for the simulation (batch/visual)'))
            if modality == 1: #batch
                params.execution.batch = True  
            elif modality == 2: #visual
                params.execution.batch = False
            else: #invalid
                print("invalid input")
            quick_setup(params)
            
        except ValueError:
            print('Not a valid input..')
            quick_setup(params)
            
            
    # Go back  
    elif choice == "0":
        try:
            print('Going back..')
            configuration(params)
            
        except ValueError:
            print('Not a valid input..')
            quick_setup(params)
         
    else:
        print('Not a valid input.. Try again')
        quick_setup(params)
        
                
# Main menu is defined:
def configuration(params: parameters.Simulation) -> None:
    """
    Configuration function (menu).
    
    Configuration works as the main menu.
    From here, user can:
       Display current parameters.
       Quick or advanced setup of the simulation.
       Running and getting simulation results.
       Terminate the program.
    
    Parameters
    ----------
    - "params": An instance of the class "Simulation" from the module "parameters"
    
    Return
    ------
    No Return value.
    
    """
    
    print('-------------------------------------------------------------------')
    print(f'''
 [1] - Display Parameters
 [2] - Quick Setup
 [3] - Advanced Setup
 [4] - Run
 [5] - Reset parameters to default
 [0] - Exit''')
    
    # Prompt user for an integer input to execute one of the four options
    choice = input('\n What would you like to do?: ')
        
    # Display Parameters
    if choice == "1":
        print(f'You selected menu {choice}.\n')   
        display_parameters(params)
        configuration(params)
        
        
    # Run Quick setup configuration
    elif choice == "2":
        print(f'You selected menu {choice}.')
        quick_setup(params)
        
        
    # Run Advanced setup configuration
    elif choice == "3":
        print(f'You selected menu {choice}.')
        am.advanced_menu(params)
        
        
    # Running the simulation and running reporting menu
    elif choice == "4":
        print(f'You selected menu {choice}.')
        sim_results = simulation.run(params)
            
        # Run reporting menu             
        rm.reporting_menu(params, sim_results)
    
    # Reset Parameter Values
    elif choice == "5":
        params = parameters.Simulation()
        print('Parameters were successfully reset!')
        configuration(params)
        
    
        # Terminate Program
    elif choice == "0":
        print(f'Now Exiting...')
        time.sleep(1)
        quit()
        
        
    else: # If any other input than 1,2,3,4,0
        print('Not a valid entry point..')
        configuration(params)    

if __name__ == '__main__':
    params = parameters.Simulation()
    display_parameters(params)
    ascii_text()
    configuration(params)
