# This script will pass a local variable to another function

# Reference
  # Stackoverflow
  # https://stackoverflow.com/questions/16043797/how-can-i-pass-information-out-of-a-function-how-can-i-use-a-functions-local-v

def defineAlist():
    local_list =['1', '2', '3']
    print("QA/QC: defineAlist uses: ", local_list)
    return local_list

def useTheList(passed_list):
    print("QA/QC: useTheList uses: ", passed_list)

def main():
    returned_list = defineAlist()

    useTheList(returned_list)

main()
