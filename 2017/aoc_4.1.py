# Advent of Code / Day 4 / Part 1

def main():
	passphrases = []
	with open("aoc_4.1_puzzle_input.txt") as f:
		passphrases = f.readlines()

	passphrases = [x.strip() for x in passphrases]
	answer = passphrase_validator(passphrases)

	print answer


def passphrase_validator(passphrases):
	correct_passphrases = 0
	for item in passphrases:
		word_list = item.split(" ")
		word_dict = {}
		valid = True
		for word in word_list:
			if word in word_dict:
				valid = False
			else:
				word_dict[word] = ""
		if valid:
			correct_passphrases += 1

	return correct_passphrases

main()