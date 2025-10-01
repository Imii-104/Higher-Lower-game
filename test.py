import random
import game_data
import art

def selector():
    return random.choice(game_data.data)

A_dict = selector()
B_dict = selector()

def selector_checker():
    global B_dict
    if A_dict == B_dict:
        B_dict = selector()
        return B_dict
        
selector_checker()
#print(A_dict)
#print(B_dict)

user_input = ""
def commentator():
    global user_input
    print(art.logo)
    print(f"Compare A: {A_dict['name']}, {A_dict['description']}, {A_dict['country']}")
    print(art.vs)
    user_input = input(f"With B: {B_dict['name']}, {B_dict['description']}, {B_dict['country']}:  ").lower()

commentator()
print(user_input)
