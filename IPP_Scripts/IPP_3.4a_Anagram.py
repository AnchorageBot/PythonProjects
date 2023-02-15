# This script will examine simple anagrams

# Impractical Python Projects by Lee Vaughn, pages 35-37
# Made with IDE: Mu v1.0.3, https://codewith.mu

# ATS, https://github.com/AnchorageBot/PythonProjects

word = list('stop')
print('The letters assigned to the variable *word* are:', word)

anagram = list('pots')
print('The letters assigned to the variable *anagram* are:', anagram)

print('Are the letters assigned to the variables *word* and *anagram* in the same order?', anagram == word)

word = sorted(word)

print('The letters assigned to the variable *word* when sorted in alpha order are:', word)

anagram = sorted(anagram)

print('The letters assigned to the variable *anagram*, when sorted in alpha order are:', anagram)

print('Are the letters assigned to the variables *word* and *anagram* in the same order now?', anagram == word)
