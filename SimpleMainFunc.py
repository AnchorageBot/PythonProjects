# This script is an example of a simplified main function
    # allows the script to be used as a reusable module or standalone script
        # import script as a reusable module 
            # __name__ = module's filename
        # standalone script
            # __name__ = __main__
        # from the command line
            # python3 SimpleMainFuncPlus.py

from time import sleep

print("This is an example of a simplified main function\n")

print("the if conditional, __name__value__ , is set to ...", __name__)
print("\n")

def process_data(data):
    """this function simulates processing data"""
    print ("Starting data processing ...")
    modified_data = data + " has been modified"
    sleep(3)
    print("Data processing complete")
    return modified_data
    
def read_data_from_web():                       
    """this function simulates reading data from the web"""
    print("Reading data from the web")
    data = "Data from the web"
    return data
    
def write_data_to_database(data):               
    """this function simulates writing data to a database"""
    print("Writing data to database...")
    sleep(3)
    print(data)

def main():
    """this function calls the various script functions"""
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_database(modified_data)
    
if __name__ == "__main__":                      # when the if statement evaluates True, main() is executed
    main()  
