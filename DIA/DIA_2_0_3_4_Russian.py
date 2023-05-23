# This script will explore testing lists for even & oddness

# References
  # Dive into Algorithms, https://nostarch.com/Dive-Into-Algorithms
  # Automate the Boring Stuff with Python, https://automatetheboringstuff.com
  # Python Crash Course, https://nostarch.com/python-crash-course-3rd-edition
  # https://stackoverflow.com/questions/66317341/im-getting-the-error-typeerror-unsupported-operand-types-for-list-and

# Made with Mu 1.0.3 during May 2023
  # https://codewith.mu

list_halves = [89, 44, 22, 11, 5, 2, 1]
list_fuse = [(89, 18), (44, 36), (22, 72), (11, 144), (5, 288), (2, 576), (1, 1152)]

list_doubles = [18, 36, 72, 144, 288, 576, 1152]
list_fuse_two = [(89, 18), (44, 36), (22, 72), (11, 144), (5, 288), (2, 576), (1, 1152)]

list_odd = []
list_even = []

def test_even_odd():
    """test for even and oddness"""

    test_one = list_halves
    print("test_one index [0] search results ", test_one[0])
    print("test_one index [1] search results ", test_one[1])
    print("test_one slice [:] search results ", test_one[:], "\n")


    test_two = list_fuse
    print("test_two index [0] search results ", test_two[0])
    print("test_two index [1] search results ", test_two[1])
    print("test_two index [2] search results ", test_two[2])
    print("test_two slice [:] search results ", test_two[:], "\n")

    test_three = list_halves
    for number in test_three:
        if number % 2 == 1:
            #print(f"Found odd: {number}")
            list_odd.append(number)
    print("test_three odd number search results ", list_odd)

    test_four = list_halves
    for item in test_four:
        if item % 2 == 0:
            #print(f"Found even: {item}")
            list_even.append(item)
    print("test_four even number search results ", list_even)
            
    #test_five = list_fuse_two
    #for pair in test_five:
        #if pair % 2:
            #print(f"Found odd: {pair}") 

test_even_odd()
