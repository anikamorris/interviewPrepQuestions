# Determine if a sentence is a pangram. A pangram is a sentence using every letter 
# of the alphabet at least once.
# The alphabet used consists of ASCII letters a to z, inclusive, 
# and is case insensitive. Input will not contain non-ASCII symbols.

# I don't have to do error handling for non-ASCII symbols because I'm guaranteed 
# in the problem description to not have to deal with any.
# My first instinct is to have a dictionary of all the letters, make the input 
# phrase all lowercase, and then iterate through each letter of the phrase.
# For each letter, add 1 to the value of the corresponding key in the dictionary.
# At the end, if there are any letters that have 0 as a value, return false, 
# otherwise return true
import string

def pangram(phrase):
    phrase = phrase.lower()
    letters = string.ascii_lowercase
    letter_dict = {}
    for letter in letters:
        letter_dict[letter] = 0
    for letter in phrase:
        letter_dict[letter] = 1
    return (0 not in letter_dict.values())


true_pangram = "The quick brown fox jumps over the lazy dog"
false_pangram = "The quick brown fox jumped over the lazy dog"
good_inputs = [true_pangram, false_pangram]

bad1 = "42##09!. afk ()"
bad2 = "//n \\mad \n"
bad_inputs = [bad1, bad2]

edge1 = "The quick b \n rown fox jumps over the lazy dog"
edge2 = true_pangram.upper()
edge_cases = [edge1, edge2]

#Expected: 
# True
# False
# False
# False
# True
# True

for case in good_inputs:
    print(pangram(case))

for case in bad_inputs:
    print(pangram(case))

for case in edge_cases:
    print(pangram(case))