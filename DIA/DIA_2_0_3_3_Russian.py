# This script will explore appending a global list with a while loop

# References
  # https://stackoverflow.com/questions/61325644/python-3-append-integers-on-a-list-with-while-true-loop

# Made with Mu 1.0.3 during May 2023
  # https://codewith.mu

purchase_amounts=[]
while True:
    a=input("Enter price of Items, then enter 'Done' when finished: ")
    if a=='Done':
        break
    else:
        purchase_amounts.append(a)

print(purchase_amounts)
