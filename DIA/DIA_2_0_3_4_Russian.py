# This script explores while loops that populate lists and dictionaries

# References
  # PY4E, https://www.py4e.com/html3/05-iterations
  # Python Crash Course, https://nostarch.com/python-crash-course-3rd-edition
    # https://ehmatthes.github.io/pcc/

# Made with Mu 1.0.3 during May 2023
  # https://codewith.mu

def blastOff(n):
    """This function counts down a blast off sequence"""
    while n > 0:
        print(n)
        n = n - 1
    print('\nBlastoff!')

responses = {}
def climberPeak():
    """This function tracks climbers and the mountain that they will climb""" 

    # Set a flag to indicate that polling is active.
    polling_active = True

    while polling_active:
      # Prompt for the person's name and response.
      name = input("\nWhat is your name? ")
      response = input("Which mountain would you like to climb someday? ")
    
      # Store the response in the dictionary:
      responses[name] = response
    
      # Find out if anyone else is going to take the poll.
      repeat = input("Would you like to let another person respond? (yes/ no) ")
      if repeat == 'no':
          polling_active = False
        
    # Polling is complete. Show the results.
    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(name + " would like to climb " + response + ".")
 
blastOff(10) 
climberPeak()
