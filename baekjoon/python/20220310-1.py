# 백준 1181번 - 단어 정렬
import sys
from collections import defaultdict

N = int(sys.stdin.readline())
words = defaultdict(defaultdict)
for _ in range(N):
	new_word = sys.stdin.readline().replace("\n","")
	new_word_ascii_list = []
	for a_letter in new_word:
		new_word_ascii_list.append(str(ord(a_letter)).zfill(3))
	new_word_ascii = "".join(new_word_ascii_list)
	words[len(new_word)][new_word_ascii] = new_word

for word_len in sorted(words.keys()):
	word_sequence = sorted(words[word_len].keys())
	for word_ascii in word_sequence:
		print(words[word_len][word_ascii])