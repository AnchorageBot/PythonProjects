# This script will explore how to construct simple phrase anagrams

# Impractical Python Projects by Lee Vaughn, pages 39-41
# Made with Mu v1.0.3 
    # https://codewith.mu

# Bonsai Trees
    # https://en.wikipedia.org/wiki/Bonsai

# ATS, https://github.com/AnchorageBot/PythonProjects

from collections import Counter # dictionary that counts the occurence of an item

my_bonsai_trees =  ['maple', 'oak', 'elm', 'birch', 'alder', 'blue spruce', 'pomegranate', 'maple', 'oak', 'maple']

count = Counter(my_bonsai_trees)

print("I look after a small bonsai tree forest consisting of", count, "trees")
print("")

print("Here is the url to a quick primer on bonsai trees")
print("https://en.wikipedia.org/wiki/Bonsai")
print("")

print("I employ a gardner named Foster to help me to tend to my bonsai tree forest")
print("")

name = 'foster'
word = 'forest'

print("Foster's name has the following numerical occurence of letters")
name_count = Counter(name)
print(name_count)

print("")

print("The word *Forest* has the following numerical occurence of letters")
word_count = Counter(word)
print(word_count)

print("")

word_count = Counter(word)
print("Is the numerical occurence of letters in *Foster* and *Forest* the same?")
if word_count == name_count:
#if word == name_count:
    print("Yes, they have the same numerical occurence of letters")
else: 
    print("No, they do not have the same numerical occurence of letters")
    
