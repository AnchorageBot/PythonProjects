# This function will build a user profile - arbitrary number of keyword arguments function example

# Source code/inspiration/software
    # Python Crash Course by Eric Matthews, Chapter 8, example 11+
    # Made with Mu 1.0.3 in November 2021

def build_user_profile(first, last, **user_info):   # ** command to make an empty dictionary to accept keyword arguments
    """Build a user profile"""
    profile = {}                                    # another empty dictionary to hold an entire user profile

    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():            # loop to add key-value pairs
        profile[key] = value

    return profile

user_profile_one = build_user_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile_one)

user_profile_two = build_user_profile('homer', 'simpson', location='springfield', field='applied nuclear physics')
print(user_profile_two)
