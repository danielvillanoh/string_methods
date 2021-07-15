# author: Daniel Villano-Herrera
# date: 7/13/2021

# --------------- Section 1 --------------- #

# 1 | String Methods
#
# 1 - Save your name to a variable named name.
#   a. Center that variable within 30 characters. Print it.
#   b. Print the variable in all upper case.
#   c. Print the variable in all lower case.
#   d. Print the variable capitalized (Look to documentation.)
name = "daniel"
print(name.center(30))
print(name.upper())
print(name.lower())
print(name.capitalize())
print()

# 2 | String Methods
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Find the first instance of the letter a. Print that position.
#   b. Find the first instance of the letter b. Print that position.
#   c. Find the first instance of a word of your choice. Print that position.

text = input('Enter a sentence here: ')
print('Here is the first instance of a at :', text.find('a'))
print('Here is the first instance of b at: ', text.find('b'))
print('Here is the first instance of the word "cool" at :', text.find('cool'))
print()

# 3 | String Methods
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Find the first appearance of every vowel in the text.
#   b. Using a built-in function, print the position of the vowel that shows up last.
#   c. Using a built-in function, print the position of the vowel that shows up first.
text = input('Please enter a sentence again: ')
print('The first instance of "a" is at: ', text.find('a'))
print('The first instance of "e" is at: ', text.find('e'))
print('The first instance of "i" is at: ', text.find('i'))
print('The first instance of "o" is at: ', text.find('o'))
print('The first instance of "u" is at: ', text.find('u'))

print()
# 4 | String Indexing
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Print the 0th letter of the text using string indexing.
#   b. Print the 1st, 2nd, and 3rd letters of the text using string indexing.
#   c. Print the last letter of the text using string indexing.
#       HINT: There are multiple ways of doing this. Is there a function that we can use that will find
#           the position of the last letter, or atleast one off from it?

text = input('I\'m asking you once again to enter a sentence: ')
print(text[0])
print(text[1], text[2], text[3])
print(text[- 1])
print()

# 5 | String Slicing
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Slice text from the 2nd position to the 5th. Print that.
#   b. Slice text from the 0th position to the 8th. Print that.
#   c. Slice text from 3rd position to end. Print that.
#   d. Slice text from the beginning to 5 positions before the last character. Print that.
#       HINT: Use a function to get the last position of the string.
text = input('Please enter any sentence :): ')
print(text[2:5])
print(text[0:8])
print(text[3:])
print(text[:-5])
print()
# 6 | String Slicing
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Print the text, but only every 2nd character.
#   b. Print the text, but only every 3rd character.
#   c. Print the text, but in reverse order.

text = input('One last time, enter a sentence :): ')
print(text[::2])
print(text[::3])
print(text[::-1])