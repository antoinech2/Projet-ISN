
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
current_case = [x_start,y_start]
print(x_start,y_start)

for loop in range (20):
	old_case = current_case
	direction = random.randint(1,4)
	if direction == 1:
		#Direction: Nord
		if current_case[0] > 2:
			current_case[0] -= 1
	elif direction == 2:
		#Direction: Sud
		if current_case[0] < map_size[0]-1:
			current_case[0] += 1
	elif direction == 3:
		#Direction: Est
		if current_case[1] < map_size[1]-1:
			current_case[1] += 1
	elif direction == 4:
		#Direction: Ouest
		if current_case[1] > 2:
			current_case[1] -= 1

	number_voisins = 0
	if (current_case[0]+1,current_case[1]) in path_coords:
		number_voisins +=1
	if (current_case[0]-1,current_case[1]) in path_coords:
		number_voisins +=1
	if (current_case[0],current_case[1]+1) in path_coords:
		number_voisins +=1
	if (current_case[0],current_case[1]-1) in path_coords:
		number_voisins +=1
	if (number_voisins < 2) and ((current_case[0],current_case[1]) not in path_coords):
		path_coords.append((current_case[0],current_case[1]))
		print("Succès:",current_case)
	else:
		current_case = old_case
		print("Echec:",current_case, old_case)

print(path_coords)

for row in range (1,map_size[0]+1):
	for column in range (1,map_size[1]+1):
		if (column,row) in path_coords:
			print("-", end="")
		else:
			print("0", end="")
	print("")
