# Advent of Code / Day 3 / Part 2
import math

def memory_location(mem_target):
	index = 2
	# Track our max and min x coord
	max_x = 0
	min_x = 0
	# Track our max and min y coord
	max_y = 0
	min_y = 0

	# Dict of memory:
	memory = {}
	memory["0,0"] = 1

	value = 0

	cur_x = 0
	cur_y = 0

	# Track which direction we are currently spiraling
	direction = 'E'

	# Iterate until we hit our target memory value, building a spiral grid.
	# We know to change spiral directions when we surpass the max/min in the direction we're headed.
	while value <= mem_target:
		if direction == 'E':
			cur_x += 1
			value = calculate_value(memory, cur_x, cur_y)
			memory[key_builder(cur_x, cur_y)] = value
			index += 1
			if (cur_x > max_x):
				# We're past the edge of our spiral. Start heading North.
				max_x = cur_x
				direction = 'N'
		elif direction == 'N':
			cur_y += 1
			value = calculate_value(memory, cur_x, cur_y)
			memory[key_builder(cur_x, cur_y)] = value
			index += 1
			if (cur_y > max_y):
				max_y = cur_y
				direction = 'W'
		elif direction == 'W':
			cur_x -= 1
			value = calculate_value(memory, cur_x, cur_y)
			memory[key_builder(cur_x, cur_y)] = value
			index += 1
			if (cur_x < min_x):
				min_x = cur_x
				direction = 'S'
		else: # direction == 'S'
			cur_y -= 1
			value = calculate_value(memory, cur_x, cur_y)
			memory[key_builder(cur_x, cur_y)] = value
			index += 1
			if (cur_y < min_y):
				min_y = cur_y
				direction = 'E'

	return value

def key_builder(x, y):
	return str(x) + "," + str(y)

def calculate_value(mem_dict, cur_x, cur_y):
	sum_surrounding = 0

	# Check all of our surroundings for values

	#	NW  N  NE
	#	 W val E
	#	SW  S  SE

	value_n = mem_dict.get(key_builder((cur_x), (cur_y + 1)))
	if value_n != None:
		sum_surrounding += value_n

	value_nw = mem_dict.get(key_builder((cur_x - 1), (cur_y + 1)))
	if value_nw != None:
		sum_surrounding += value_nw

	value_w = mem_dict.get(key_builder((cur_x - 1), cur_y))
	if value_w != None:
		sum_surrounding += value_w
	
	value_sw = mem_dict.get(key_builder((cur_x - 1), (cur_y - 1)))
	if value_sw != None:
		sum_surrounding += value_sw
	
	value_s = mem_dict.get(key_builder((cur_x), (cur_y - 1)))
	if value_s != None:
		sum_surrounding += value_s

	value_se = mem_dict.get(key_builder((cur_x + 1), (cur_y - 1)))
	if value_se != None:
		sum_surrounding += value_se

	value_e = mem_dict.get(key_builder((cur_x + 1), cur_y))
	if value_e != None:
		sum_surrounding += value_e

	value_ne = mem_dict.get(key_builder((cur_x + 1), (cur_y + 1)))
	if value_ne != None:
		sum_surrounding += value_ne

	return sum_surrounding

print memory_location(277678)