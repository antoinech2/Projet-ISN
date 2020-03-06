
# Algorithme de création aléatoire du chemin

# Importation des modules
import random

# Définition des constantes
map_size = (20,20)

path_coords = []

#total_possibilities = (map_size[0]-2)*2 + (map_size[1]-2)*2
#chosen_case_id = random.randint(0,total_possibilities)

if random.randint(0,1) == 1:
    if random.randint(0,1) == 1:
        x_start = 1
    else:
        x_start = map_size[0]
    y_start = random.randint(2,map_size[1]-1)
else:
    if random.randint(0,1) == 1:
        y_start = 1
    else:
        y_start = map_size[1]
    x_start = random.randint(2,map_size[0]-1)

start_coords = (x_start,y_start)
path_coords.append(start_coords)
current_case = start_coords
print(x_start,y_start)

for loop in range (20):
    direction = random.randint(1,4)
    if direction == 1:
        #Direction: Nord
        current_case = (current_case[0]-1,current_case[1])
    elif direction == 2:
        #Direction: Sud
        current_case = (current_case[0]+1,current_case[1])
    elif direction == 3:
        #Direction: Est
        current_case = (current_case[0],current_case[1]+1)
    elif direction == 4:
        #Direction: Ouest
        current_case = (current_case[0],current_case[1]-1)
    path_coords.append(current_case)

print(path_coords)
