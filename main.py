from stats import get_num_words, get_num_char

def main():
	path = "books/frankenstein.txt"
	text = get_book_text(path)
	num_words = get_num_words(text)
	char_num = get_num_char(text)
	print (f"{num_words} words found in the document")
	print (char_num)



def get_book_text(filepath):
	with open(filepath) as f:
		text = f.read()
	return text










main()
