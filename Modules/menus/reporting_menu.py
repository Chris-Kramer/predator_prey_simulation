import os, sys

sys.path.append(os.path.join("..", "..")) # For main menu
sys.path.append(os.path.join("..", "classes")) # For classes
import foxes_and_rabbits, reporting, parameters,results
import typing

def reporting_menu(params: parameters.Simulation, sim_results: results.SimulationStats) -> None:
    """reporting_menu.
This function displays the menu for reporting and summarizes results from the simulation.
The module reporting is a mock implementation.
Parameters
--------------
sim_results: The return values from the function "run" in the module "simulation"
params: An instance of the class "Simulation" from the module "parameters"
Return
--------------
No return values
Menu
--------------
Pick an option from above:
[1] summary
    this prints a summary of the simulation results
[2] plot pop.size/time
    plots population sizes against time
[3] plot lifespan
    plot lifespans across population individuals
[4] plot energy
    plots the total energy over the life of each individual
[5] plot kills distribution
    shows the distribution of kills
[0] Quit
    takes the user back to reporting_menu"""
    
    print("""
[1] Summary
[2] Plot pop. size/time")
[3] Plot lifespan
[4] plot energy
[5] plot kills distribution
[0] Quit""")
    
    choice = input("Pick an option from above [?]\n")
    if choice == "1":
        reporting.print_summary(sim_results)
        reporting_menu(params, sim_results)
    elif choice == "2":
        reporting.plot_pop_size(sim_results)
        reporting_menu(params, sim_results)
    elif choice == "3":
        reporting.plot_lifespan(sim_results)
        reporting_menu(params, sim_results)
    elif choice == "4":
        reporting.plot_energy(sim_results)
        reporting_menu(params, sim_results)
    elif choice == "5":
        reporting.plot_kills(sim_results)
        reporting_menu(params, sim_results)
    elif choice == "6":
        print(quit)
    elif choice == "0":
        print('Going back')
        foxes_and_rabbits.configuration(params)
    else:
        print("input not valid")
        reporting_menu(params, sim_results)