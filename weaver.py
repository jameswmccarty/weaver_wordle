#!/usr/bin/python

# for https://wordwormdormdork.com/

start, end = "wish","star"

word_list = set()
with open("enable1.txt","r") as infile:
	word_list = { line.strip() for line in infile.readlines() if len(line.strip()) == len(start) }

def diff_count(w1,w2):
	count = 0
	for idx,char in enumerate(w1):
		if w2[idx] != char:
			count += 1
	return count

q = [(start,'')]
seen = set()
seen.add(start)
while len(q) > 0:
	current, chain = q.pop(0)
	if current == end:
		print(chain[1:]+','+end)
		exit()
	nexts = [ word for word in word_list if diff_count(word,current) == 1 ]
	for next in nexts:
		if next not in seen:
			q.append((next,chain+','+current))
			seen.add(next)

