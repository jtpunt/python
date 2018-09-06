# Author: Jonathan Perry
# Date: 9/6/2018
import re
import math
# Iterates through n/2 characters of the string str, where the first half of the characters are checked
# against the 2nd half of characters (where the 2nd half is in reversed order) match the first half of characters.
# For example, assume we split the string in 2 seperate arrays, i and j. By using the ceil function, we can safely assume
# both halves will have the same # of elements, regardless of whether or not our string has an even or odd # of characters.
# i = [0,   1,   2, ... ceil(n / 2)] (first half - forward order)
# j = [n, n-1, n-2, ... ceil(n / 2)] (second half -  reverse order)
# If our our string is a palindrome, then arrays i and j will contain the same elements in the same exact order and the 
# function will return true. If it does not contain the same elements, the function will return false.
def isPalidrome(str):
	length=len(str) - 1
	for _ in (i for i in range(0, math.ceil(length / 2)) if str[i] != str[length-i]):
		return False
	return True

# first re call removes spaces, second re call removes non-alphabetical characters
def cleanStr(uncleanStr):
	return re.sub(r'[^a-zA-Z]', '', re.sub(r'\s+', '', uncleanStr.lower())) 
	
def main():
	sentence="A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!"
	sentence=cleanStr(sentence)
	print(isPalidrome(sentence))


if __name__ == "__main__":
	main()