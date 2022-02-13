import sys
import os
sys.path.append(os.path.join("..", "classes"))
from results import SimulationStats
from matplotlib import pyplot as plt
import numpy as np

def print_summary(results: SimulationStats) -> None:
  """
  Prints a summary of the simulation results and basic statistics.
  
  Parameters
  ----------
  - results: An instance of the class SimulationStats from the module results
  
  Return
  ------
  No return value
  """
  # ------ Headers ------
  col_1 = "             " # Header column 1
  col_2 = " foxes "       # Header column 2
  col_3 = " rabbits "     # Header column 3
  col_4 = " aggreated "   # Header column 4

  #------ Inner functions ------ 
  def _line_break(col_1, col_2, col_3, col_4):
    """
    Prints a line break with the appropriate length according to the length of the headers
    """
    print("-"*len(col_1) + "+" + "-"*len(col_2) + "+" + "-"*len(col_3) + "+" + "-"*len(col_4) + "|")
    
  def _format_cell(val, col, padding="l"):
    """
    Format a cell value so its layout fits the table. Defaults to padding (space) on left side of value.
    """
    # Padding on right side
    if padding.lower() == "r" or padding.lower() == "right":
      return val + " " * (len(col) - len(val)) + "|"
    # Padding on left side
    else:
      return " " * (len(col) - len(val)) + val + "|"
            
  def __print_row(cell_1, cell_2, cell_3, cell_4):
    """
    Prints a row containg four cells, that are formatted to fit the table.
    IMPORTANT: It relies on variables in the outer scope, it CANNOT be used without these.
    """
    print(_format_cell(cell_1, col_1, padding= "r") + _format_cell(cell_2, col_2) + _format_cell(cell_3, col_3) + _format_cell(cell_4, col_4))
  
  # Save objecs on variables for readability
  fox_stats = results.foxes
  rabbit_stats = results.rabbits
  
  #------- Print table -------
  # Header
  print(f"{col_1}|{col_2}|{col_3}|{col_4}|")
  # Line break
  _line_break(col_1, col_2, col_3, col_4)
  # Row 1
  __print_row("Individuals", str(fox_stats.total), str(rabbit_stats.total),
                str(fox_stats.total + rabbit_stats.total))
  # Row 2
  step_fewest_foxes = min(fox_stats.size_per_step)
  step_fewest_rabbits = min(rabbit_stats.size_per_step)
  __print_row(" min. energy", str(step_fewest_foxes), str(step_fewest_rabbits),
              str(step_fewest_foxes + step_fewest_rabbits))
  # Row 3
  step_most_foxes = max(fox_stats.size_per_step)
  step_most_rabbits = max(rabbit_stats.size_per_step)
  __print_row(" max. energy", str(step_most_foxes), str(step_most_rabbits),
              str(step_most_foxes + step_most_rabbits))
  # Row 4
  avg_foxes = round(sum(fox_stats.size_per_step)/len(fox_stats.size_per_step), 2)
  avg_rabbits = round(sum(rabbit_stats.size_per_step)/len(rabbit_stats.size_per_step), 2)
  avg_total = round(avg_foxes + avg_rabbits, 2)
  __print_row(" avg. energy", str(avg_foxes), str(avg_rabbits),
              str(avg_total))        
    
  # Line break
  _line_break(col_1, col_2, col_3, col_4)
    
  # Row 5
  dead_foxes = fox_stats.dead_by_old_age + fox_stats.dead_by_predation + fox_stats.dead_by_starvation
  dead_rabbits = rabbit_stats.dead_by_old_age + rabbit_stats.dead_by_predation + rabbit_stats.dead_by_starvation
  __print_row("deaths", str(dead_foxes), str(dead_rabbits),
              str(dead_foxes + dead_rabbits))
  # Row 6
  __print_row(" old age", str(fox_stats.dead_by_old_age), str(rabbit_stats.dead_by_old_age),
              str(fox_stats.dead_by_old_age + rabbit_stats.dead_by_old_age))         
  # Row 7
  __print_row(" starvation", str(fox_stats.dead_by_starvation), str(rabbit_stats.dead_by_starvation),
              str(fox_stats.dead_by_starvation + rabbit_stats.dead_by_starvation))
  # Row 8
  __print_row(" predation", str(fox_stats.dead_by_predation), str(rabbit_stats.dead_by_predation),
              str(fox_stats.dead_by_predation + rabbit_stats.dead_by_predation))
  # Line break
  _line_break(col_1, col_2, col_3, col_4)  

def plot_pop_size(results: SimulationStats) -> None:
  """
  Plots population sizes against time. 
  """
  # Plot
  plt.figure()
  combined_pop = [r_size + f_size for r_size, f_size in zip(results.rabbits.size_per_step, results.foxes.size_per_step)]
  plt.plot(results.rabbits.size_per_step, label = "Rabbits", color="cyan")
  plt.plot(results.foxes.size_per_step, label = "Foxes", color="orange")
  plt.plot(combined_pop, label = "Combined population", color = "green")
  # Legend and labels
  plt.legend()
  plt.ylabel("Population Size")
  plt.xlabel("Simulation Step")
  plt.title("Population Size pr. step")
  plt.show()

def plot_lifespan(results: SimulationStats) -> None:
  """
  Plots lifespans across population idividuals. 
  """
   # Plot
  fig, (ax1, ax2) = plt.subplots(2,1)
  fig.suptitle('Lifespan Foxes and Rabbits')

  # Rabbits plot
  bin_r = np.arange(0, max(results.rabbits.age_at_death) + 1) + 0.5
  # Plot and ticks
  ax1.hist(results.rabbits.age_at_death, bins = bin_r, ec="grey", color="cyan")
  ax1.set_xticks(range(max(results.rabbits.age_at_death) + 1))
  # Labels and title
  ax1.set_ylabel("Frequency")
  ax1.title.set_text("Rabbits")

  # Foxes plot
  bin_f = np.arange(0, max(results.foxes.age_at_death) + 1) + 0.5
  # Plot and ticks
  ax2.hist(results.foxes.age_at_death, bins = bin_f, ec="grey", color="orange")
  ax2.set_xticks(range(max(results.foxes.age_at_death) + 1))
  # Labels and title
  ax2.set_ylabel("Frequency")
  ax2.set_xlabel("Age at death")
  ax2.title.set_text("Foxes")
  plt.show()

  

def plot_energy(results: SimulationStats) -> None:
  """
  Plots the total energry over the life of eah individual. 
  """

  #Plot
  plt.figure()
  plt.plot(results.foxes.avg_energy_per_step, label = "Foxes", color="orange")
  plt.plot(results.rabbits.avg_energy_per_step, label = "Rabbits", color="cyan")
  plt.plot(results.avg_energy_per_step, label = "Total", color = "green")
  # Legend and labels
  plt.legend()
  plt.ylabel("Average Energy")
  plt.xlabel("Simulation Step")
  plt.title("Energy per step")
  plt.show()
  
def plot_kills(results: SimulationStats) -> None:
  """
  Displays the distribution of kills
  """
  # Colormap and Colobar
  max_kills = max([max(row) for row in results.kills_per_patch]) # Used for setting the ticks in the colorbar
  min_kills = min([min(row) for row in results.kills_per_patch])
  plt.figure() # Initialize
  plt.pcolormesh(results.kills_per_patch, cmap="binary") # Colormap
  plt.colorbar(ticks = range(min_kills, max_kills + 1), label = "Amount of Kills")
  
  # Title and labels
  plt.title("Spatial distribution of deaths by predation")
  plt.ylabel("South <---------------> North")
  plt.xlabel("West <---------------> East")
  
  # Ticks - remove them
  plt.xticks(ticks = [])
  plt.yticks(ticks = [])
  plt.show()

if __name__ == "__main__":
  pass

