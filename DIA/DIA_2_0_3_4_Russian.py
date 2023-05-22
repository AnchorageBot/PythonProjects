# This script will explore testing lists for even & oddness

# References
  # Dive into Algorithms, https://nostarch.com/Dive-Into-Algorithms
  # Automate the Boring Stuff with Python, https://automatetheboringstuff.com
  # Python Crash Course, https://nostarch.com/python-crash-course-3rd-edition

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

    #half_double = half_double.loc[half_double[0]%2==1,:]

    test = list_halves
    print("test index [0] search results ", test[0])
    print("test index [1] search results ", test[1])
    print("test slice [:] search results ", test[:], "\n")


    test_two = list_fuse
    print("test_two index [0] search results ", test_two[0])
    print("test_two index [1] search results ", test_two[1])
    print("test_two index [2] search results ", test_two[2])
    print("test_two slice [:] search results ", test_two[:], "\n")


    test_three = list_doubles
    #while test_three[:] :
        #print("test_three search results ", test_three)
        #test_three = test_three{:]%2==1
        #list_odd.append(test_three)

    #return(test_three)
    #print(test_three)
    #print(list_odd)


    #test_four = list_fuse_two
    #while test_four[:] :
        #print(test_four)
        #test_four = test[:]%2==0
        #list_odd.append(test_four)

    #return(test_four)
    #print(test_four)
    #print(list_even)

test_even_odd()
