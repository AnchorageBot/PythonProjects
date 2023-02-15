# This script will ask a user to input a word, then look for anagrams, after loading a text file as a dictionary
    # elvis and lives are examples of anagrams

# Source code/inspiration/software/text file
    # Impractical Python Projects by Lee Vaughn, Chapter 3, Project 4+
    # Made with Mu 1.0.3 in November 2021
    # Source of text file used as dictionary for analysis is ver 6.02
        # URL http://wordlist.aspell.net/12dicts/
        # Text file to analyze 2of4brif.txt
        # Text file, 2of4brif.txt, is stored in the same folder as this script

# Libraries needed to run this script
import sys                                                      # accesses error handling code
import time                                                     # helps with code optimization by timing our script's run time

start_time = time.time()                                        # start the script runtime clock

# Dictionary function
def loadDictionary(file):
    """Open a text file and load as lower case strings"""
    try:
        with open(file) as in_file:
            loaded_text = in_file.read().strip().split('\n')    # processes text file: whitespace, separate lines, added to list
            loaded_text = [x.lower() for x in loaded_text]      # list words are shifted to lower case
            return loaded_text
    except IOError as e:
        print("{}\nError opening {}. Terminating program" .format(e,file), file=sys.stderr)
        sys.exit(1)

# Anagram function
def anagramFinder(file_to_analyze):
    """Find anagrams in a text tile"""
    word_list = loadDictionary(file_to_analyze)                 # call the dictionary function
    anagram_list = []
    
    name = input("Please enter a word and I will look for an anagram\n")    # name or word to be analyzed
    print("Input name = {}".format(name))
    name = name.lower()
    
    name_sorted = sorted(name)
    for word in word_list:
        word = word.lower()
        if word !=name:
            if sorted(word) == name_sorted:
                anagram_list.append(word)
                
    print()                                                     # print out list of anagrams
    if len(anagram_list) == 0:
        print("I could not find an anagram for this word")
    else:
        print("Anagrams =", *anagram_list, sep='\n')
        
# Main
anagramFinder('2of4brif.txt')                                   # Specify the text file to be analyzed/used as a dictionary ('YourChoice.txt')

end_time = time.time()                                          # stop the script runtime clock & display the results
print("\nSpeed_check: script run time is {} seconds".format(end_time - start_time))
