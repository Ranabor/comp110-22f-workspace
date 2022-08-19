"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730575704"

from re import X


print("Enter a 5 character word:", end=" ")
word_choice = input()
if len(word_choice) != 5:
        print ("Error: Word must contain 5 characters")
        exit()

print("Enter a single character:", end=" ")
char_choice = input()
if len(char_choice) != 1:
        print ("Error: Character must be a single character")
        exit()

print("Searching for", char_choice, "in", word_choice)


char_count = 0

if word_choice[0] == char_choice:
    print(char_choice, "found at index 0")
    char_count += 1

if word_choice[1] == char_choice:
    print(char_choice, "found at index 1")
    char_count += 1

if word_choice[2] == char_choice:
    print(char_choice, "found at index 2")
    char_count += 1

if word_choice[3] == char_choice:
    print(char_choice, "found at index 3")
    char_count += 1

if word_choice[4] == char_choice:
    print(char_choice, "found at index 4")
    char_count += 1

if char_count > 0:
    if char_count == 1:
        print (char_count, "instance of", char_choice, "found in", word_choice)
    if char_count > 1:
        print (char_count, "instances of", char_choice, "found in", word_choice)
else:
    print ("No instances of", char_choice, "found in", word_choice)



"""What I originally did before I read 'no loops'"""
# index_count = 0
# for x in word_choice:
#     if x == char_choice:
#         print(char_choice, "found at index", index_count)
#         char_count += 1
#     index_count += 1
# print(char_count, "instances of", char_choice, "found in", word_choice)
        
