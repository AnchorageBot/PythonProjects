# This function will loop a greeting - optional argument example

# Source code/inspiration/software
    # Python Crash Course by Eric Matthews, Chapter 8, example 6+
    # Made with Mu 1.0.3 in October 2021

def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your full name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    m_name = input("Middle name: ")
    if m_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, m_name, l_name)
    print("\nHello, " + formatted_name + "!")
