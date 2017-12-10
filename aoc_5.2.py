# Advent of code / Day 5 / Part 1

def main():
	jump_list = []
	with open("aoc_5.2_puzzle_input.txt") as f:
		jump_list = f.readlines()

	jump_list = [x.strip() for x in jump_list]
	jump_list = [int(i) for i in jump_list]

	answer = jump_calculator(jump_list)

	print answer

def jump_calculator(jump_list):
	cur_index = 0
	total_jumps = 0
	while ((cur_index >= 0) and (cur_index < len(jump_list))):
		next_index = cur_index + jump_list[cur_index]
		if (jump_list[cur_index] >= 3):
			jump_list[cur_index] -= 1
		else:
			jump_list[cur_index] += 1
		cur_index = next_index
		total_jumps += 1

	return total_jumps

main()