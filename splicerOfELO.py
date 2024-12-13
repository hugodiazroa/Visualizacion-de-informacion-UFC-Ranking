#in this file we will read the data from the csv file "large_dataset.csv"
#we will output just the data that we need for the "hito-2.ipynb" file into a "elo.csv" file
#we will create a new csv file "elo.csv" that will contain the following columns:
"""
1. "id" - the id of the point to plot (a hash of the name of the player and the date of the fight)
2. "result" - the result of the fight (1 if the player won, 0 if the player lost)
3. "date" - the date of the fight
4. "name" - the name of the player
5. "elo" - the original elo of the player
6. "elo_opp" - the original elo of the opponent
7. "elo_new" - the new elo of the player (this is redundant, but it will make it easier to plot the data)
8. "elo_opp_new" - the new elo of the opponent (this is redundant, but it will make it easier to plot the data)
9. "HD" - the HD rank of the player (
10. "isRed"  - 1 if the player is red, 0 if the player is blue
"""

import pandas as pd
import numpy

#we open the file "large_dataset.csv"
data = pd.read_csv("large_dataset.csv")

#we create the new csv file "elo.csv"
elo = pd.DataFrame(columns=["id", "result", "date", "name", "elo", "elo_opp", "elo_new", "elo_opp_new", "HD"])

#we migrate the red corners


#we migrate the blue corners