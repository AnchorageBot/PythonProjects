# This script will load a text file and attempt to find palindromes

# Source code/inspiration/software/text file 
    # Impractical Python Projects by Lee Vaughn, Chapter 2, Project 2+
    # Made with Mu 1.0.3 in November 2021
    # Source of text file used for palindrome analysis is ver 6.02
        # URL http://wordlist.aspell.net/12dicts/
        # Text file to analyze 2of4brif.txt
        # Text file, 2of4brif.txt, is stored in the same folder as this script

# Libraries needed to run this script
import sys                                                      # accesses error handling code

# Dictionary function
def loadDictionary(file):
    """Open a text file and load lower case strings"""
    try:
        with open(file) as in_file:
            loaded_text = in_file.read().strip().split('\n')    # processes text file: whitespace, separate lines, added to list
            loaded_text = [x.lower() for x in loaded_text]      # list words are shifted to lower case
            return loaded_text
            print("done")
    except IOError as e:
        print("{}\nError opening {}. Terminating program" .format(e,file), file=sys.stderr)
        sys.exit(1)
    print("done")

# Palindrome function
def palindromeFinder(file_to_analyze):
    """Find pallindromes in a text file"""
    word_list = loadDictionary(file_to_analyze)
    pali_list = []

    for word in word_list:
        if len(word) > 1 and word == word[::-1]:
            pali_list.append(word)

    print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
    print(*pali_list, sep = '\n')

palindromeFinder('2of4brif.txt')
