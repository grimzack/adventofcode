# Advent of Code / Day 3 / Part 1
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
	memory[1] = [0,0]

	cur_x = 0
	cur_y = 0

	# Track which direction we are currently spiraling
	direction = 'E'

	# Iterate until we hit our target memory location, building a spiral grid.
	# We know to change spiral directions when we surpass the max/min in the direction we're headed.
	while index <= mem_target:
		if direction == 'E':
			# do something
			cur_x += 1
			memory[index] = [cur_x, cur_y]
			index += 1
			if (cur_x > max_x):
				# We're past the edge of our spiral. Start heading North.
				max_x = cur_x
				direction = 'N'
		elif direction == 'N':
			cur_y += 1
			memory[index] = [cur_x, cur_y]
			index += 1
			if (cur_y > max_y):
				max_y = cur_y
				direction = 'W'
		elif direction == 'W':
			cur_x -= 1
			memory[index] = [cur_x, cur_y]
			index += 1
			if (cur_x < min_x):
				min_x = cur_x
				direction = 'S'
		else: # direction == 'S'
			cur_y -= 1
			memory[index] = [cur_x, cur_y]
			index += 1
			if (cur_y < min_y):
				min_y = cur_y
				direction = 'E'

	target_coord = memory[mem_target]

	return man_dist(target_coord[0], target_coord[1])

def man_dist(x, y):
	return (abs(x) + abs(y))


print memory_location(1)
print memory_location(12)
print memory_location(23)
print memory_location(277678)