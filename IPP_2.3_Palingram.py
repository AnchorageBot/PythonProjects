# This script will load a text file and attempt to find word-pair palingrams within the file
    # nurses run and stir grits are examples of palingrams
    # This script is amazing however it can be optimized to run faster
        # We will time the script's runtime and use it as a baseline measurement for future efforts

# Source code/inspiration/software/text file
    # Impractical Python Projects by Lee Vaughn, Chapter 2, Project 3+
    # Made with Mu 1.0.3 in November 2021
    # Source of text file used for palindrome analysis is ver 6.02
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

# Palingram function
def find_palingrams(file_to_analyze):
    """Find palingrams in a text file"""
    word_list = loadDictionary(file_to_analyze)                             # call the dictionary function
    pali_list = []
    
    for word in word_list:                                                  # loop through the list
        end = len(word)
        rev_word = word[::-1]
        
        if end > 1:
            for i in range(end):                                            # the palingram magic happens here
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                    pali_list.append((rev_word[:end-i],word))
                    
    return pali_list
    
# Main
palingrams = find_palingrams('2of4brif.txt')                                # Specify the text file to be analyzed ('YourChoice.txt')
palingrams_sorted = sorted(palingrams)                                      # Sort palingrams on first_word

print("\nNumber of palingrams ={}\n".format(len(palingrams_sorted)))        # Display list of palingrams found
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))
    
end_time = time.time()                                                      # stop the script runtime clock & display the results
print("\nSpeed_check: script run time is {} seconds".format(end_time - start_time))
