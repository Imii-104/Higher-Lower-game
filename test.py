import random
import game_data
import art

game_over = False

def selector():
    return random.choice(game_data.data)

A_dict = selector()
B_dict = selector()
score = 0


def selector_checker():
    global B_dict
    if A_dict == B_dict:
        B_dict = selector()
        return B_dict
 
dict_map = {
    "A": A_dict,
    "B": B_dict
}

#print(A_dict)
#print(B_dict)

user_input = ""
def commentator():
    global user_input
    print(art.logo)
    print(f"Compare A: {A_dict['name']}, {A_dict['description']}, {A_dict['country']}")
    print(art.vs)
    user_input = input(f"With B: {B_dict['name']}, {B_dict['description']}, {B_dict['country']}:  ").upper()

#print(A_dict['follower_count'])
#print(B_dict['follower_count'])

answer = None
def answer_checker():
    global answer, A_dict, B_dict
    if A_dict['follower_count'] > B_dict['follower_count']:
        answer = A_dict
    elif A_dict['follower_count'] < B_dict['follower_count']:
        answer = B_dict
    return answer


def answer_declarer():
    global score, A_dict, game_over
    if dict_map[user_input] == answer:
        print(f"You are correct! {answer['name']} is the correct answer.")
        score += 1
        print(f"Current score: {score}")
        
    else:
        print(f"You have made an invalid choice! \nFinal score: {score}")
        game_over = True
             
    return score
    

while not game_over:
   if answer:
       A_dict = answer
   else:
       A_dict = selector()
   B_dict = selector()
   print(A_dict)
   print(B_dict)
   selector_checker()
   dict_map = {
    "A": A_dict,
    "B": B_dict
}
   commentator()
   answer_checker()
   answer_declarer()
   