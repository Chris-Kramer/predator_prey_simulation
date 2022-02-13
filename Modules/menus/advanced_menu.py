import os
import sys
import config_menus as cm
import typing

sys.path.append(os.path.join("..", "..")) # For main menu
sys.path.append(os.path.join("..", "classes")) # For classes

import parameters
import foxes_and_rabbits

def advanced_menu(sim_parameters: parameters.Simulation) -> None:
    """Display advanced menu
        This function displays the advanced menu and activates submenus based on user input.

        Parameters
        ------------
        - sim_parameters: An instance of the class "Simulation" from the module "parameters".

        Return
        ------------
        No return value

        Example
        ------------
        >>> import parameters
        >>> params = parameters.Simulation()
        >>> advanced_menu(params)
        Choose parameter to customize: 
            [1] World 
            [2] Rabbit population 
            [3] Fox population 
            [4] Execution 
            [0] Done/Go back
        Enter selection:
        """
    #Choice prompt
    print("Choose parameter to customize:" +
          "\n\t[1] World" +
          "\n\t[2] Rabbit population" +
          "\n\t[3] Fox population" +
          "\n\t[4] Execution" +
          "\n\t[0] Done/Go back")
    choice = input("Enter selection: ")
    # Configure world
    if choice == "1":
        cm.configure_world(sim_parameters)        
    # Configure rabbits population
    elif choice == "2":
        rabbits = sim_parameters.rabbits
        cm.configure_species(sim_parameters, rabbits)
    #configure foxes population
    elif choice == "3":
        foxes = sim_parameters.foxes
        cm.configure_species(sim_parameters, foxes)
    # configure execution    
    elif choice == "4":
        cm.configure_execution(sim_parameters)
    #Return to main menu    
    elif choice == "0":
        foxes_and_rabbits.configuration(sim_parameters)
    #Invalid input
    else:
        print("invalid choice")
        advanced_menu(sim_parameters)