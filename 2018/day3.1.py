# Advent of Code - Day 3 - Part 1
import re

def main():
	# Need to sort our input into something we can use.
	# Keep track of it as rectangles and count the overlaps
	regex = r"#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9])x([0-9])"
	
	# rect_list will be a list of rectangles of the form:
	# (row, column, height, width)
	rect_list = []

	filename = "test_input.txt"
	with open(filename) as f:
		all_lines = f.readlines()

		for line in all_lines:
			match = re.match(regex, line)
			rect_list.append((int(match.group(2)), int(match.group(3)), int(match.group(4)), int(match.group(5))))


	# Now we have a list of tuples describing all of our rectangles. 
	# Need to figure out how many "squares" are overlapped by at least 2 rect
main()


# print("Match.group0 =", match.group(0), "group1 =", match.group(1))
# print("group2 =", match.group(2), "group3 =", match.group(3))
# print("group4 =", match.group(4), "group5 =", match.group(5))

	# Match.group0 = #1 @ 1,3: 4x4 group1 = 1
	# group2 = 1 group3 = 3
	# group4 = 4 group5 = 4
	# Match.group0 = #2 @ 3,1: 4x4 group1 = 2
	# group2 = 3 group3 = 1
	# group4 = 4 group5 = 4
	# Match.group0 = #3 @ 5,5: 2x2 group1 = 3
	# group2 = 5 group3 = 5
	# group4 = 2 group5 = 2
