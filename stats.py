def get_num_words(text):
	words = text.split()
	return len(words)

def get_num_char(text):
	total_count = {}
	for char in text:
		lowered = char.lower()
		if lowered in total_count:
			total_count[lowered] += 1
		else:
			total_count[lowered] = 1
	return total_count
