# Advent of Code 2018 - Day 2 - Part 1

def main():
	# Task: Go through box IDs, count whether letters occur exactly 2 or 3 times.
	# Strategy: Go through each box ID, count occurrences of letters by storing in dict
	# 	Then, go through dict and see how many letters have exactly 2 or 3 occurrences. 
	#	If a box ID does, increment 2x or 3x counters.

	letter_dict = {}
	num_two = 0
	num_three = 0

	counted_two = False
	counted_three = False

	filename = "day2_input.txt"
	with open(filename) as f:
		for line in f.readlines():
			for letter in line:
				letter_dict[letter] = letter_dict.get(letter, 0) + 1
			for key in letter_dict:
				if letter_dict[key] == 2:
					if not counted_two:
						num_two += 1
						counted_two = True
				if letter_dict[key] == 3:
					if not counted_three:
						num_three += 1
						counted_three = True

			print(letter_dict)
			letter_dict = {}
			counted_two = False
			counted_three = False

	answer = num_two * num_three

	return answer


gogogo = main()

print(gogogo)
