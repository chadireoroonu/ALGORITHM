import sys
sys.stdin = open("input.txt")

word1 = sys.stdin.readline()
word2 = sys.stdin.readline()

if len(word1) < len(word2):
    word1, word2 = word2, word1

