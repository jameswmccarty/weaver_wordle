#!/usr/bin/python

# for https://wordwormdormdork.com/

start, end = "stop","sign"

word_list = set()
with open("enable1.txt","r") as infile:
	word_list = { line.strip() for line in infile.readlines() if len(line.strip()) == len(start) }
lower_alpha = [ chr(_) for _ in range(97,97+26) ]

# Return True if words differ by 1 letter
def diff_count_of_one(w1,w2):
	count = 0
	for idx,char in enumerate(w1):
		if w2[idx] != char:
			count += 1
		if count > 1:
			return False
	if count == 1:
		return True
	return False

# Return words that are valid and only differ by one character
def next_poss_words(word):
	next_words = []
	for idx,char in enumerate(word):
		for c in lower_alpha:
			if c != char:
				next_word = word[0:idx]+c+word[idx+1:]
				if next_word in word_list:
					next_words.append(next_word)
	return next_words

q = [(start,'')]
seen = set()
seen.add(start)
while len(q) > 0:
	current, chain = q.pop(0)
	if current == end:
		print(chain[1:]+','+end,chain.count(","))
		exit()
	nexts = [ word for word in next_poss_words(current) if word not in seen ]
	for next in nexts:
		q.append((next,chain+','+current))
		seen.add(next)

