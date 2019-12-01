# Advent of Code - Day 2 - Part 2

def main():
	# Go through each string and compare letters. 
	# If we find one different, remember that until we find another different.
	# If we don't find more than one different, return that letter.

	num_diffs = 0
	diff_index = 0
	same_letters = ''

	filename = "day2_input.txt"
	with open(filename) as f:
		all_input = f.read().splitlines()
		for i in range(len(all_input) - 1):
			cur_id = all_input[i]
			for j in range(i + 1, len(all_input)):
				# print("i =", i, "j =", j, "all_input =", all_input)
				next_id = all_input[j]
				# print("i =", i, "j =", j, "cur_id =", cur_id, "next_id =", next_id)
				for k in range(len(cur_id)):
					# print("cur_id[k] =", cur_id[k], "next_id[k] =", next_id[k])
					# print("num_diffs =", num_diffs, "diff_index =", diff_index, "same_letters =", same_letters)

					if cur_id[k] == next_id[k]:
						continue
					else:
						if num_diffs == 0:
							diff_index = k
							num_diffs = 1
							continue
						else: # num_diffs == 1:
							diff_index = -1
							num_diffs += 1
							continue
				if diff_index > 0:
					same_letters = cur_id[:diff_index] + cur_id[(diff_index + 1):]
					# print("ABOUT TO BREAK!\n", "num_diffs =", num_diffs, "diff_index =", diff_index, "same_letters =", same_letters)
					break
				num_diffs = 0
				diff_index = 0

	return same_letters

answer = main()
print(answer)