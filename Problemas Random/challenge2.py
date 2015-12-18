# "Anagram": An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase using all the original letters exactly once; for example, the letters from 'icon' can be rearranged into 'coin'.

# Devise a function that takes one parameter W and returns all the anagrams for W from the file wl.txt.

# anagrams("beat") should return:
# ["beat", "beta", "bate"]

# =====================
# Test cases:

# anagrams("able") should return:
# ['abel', 'able', 'bale', 'beal']

# anagrams("apple") should return:
# ['appel', 'apple']

# anagrams("spot") should return:
# ['post', 'pots', 'spot', 'stop', 'tops']

# anagrams("reset") should return:
# ['reset', 'steer', "trees"]

with open('wl.txt') as f:
    fileContent = map(lambda x: x.strip(), f.readlines())
# print filter(lambda x: sorted(x) == sorted('reset'), fileContent)
print [e for e in fileContent if sorted(e) == sorted('reset')]