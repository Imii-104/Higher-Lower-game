import random
import game_data
import art
import threading

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

user_input = ""
timeout = False  # flag to track timeout


def time_up():
    """Called after 10 seconds if user hasn't entered input."""
    global timeout
    timeout = True
    print("\n⏰ Time’s up! You didn’t enter any input.")
    

def commentator():
    global user_input, timeout
    print(art.logo)
    print(f"Compare A: {A_dict['name']}, {A_dict['description']}, {A_dict['country']}")
    print(art.vs)
    print(f"With B: {B_dict['name']}, {B_dict['description']}, {B_dict['country']}")
    print("⏳ You have 10 seconds to answer!")
    
    # start timer
    timer = threading.Timer(10.0, time_up)
    timer.start()
    
    user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    # cancel timer if user entered input in time
    if not timeout:
        timer.cancel()


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
    if timeout:  # end game if time ran out
        game_over = True
        print(f"Game over! You ran out of time. Final score: {score}")
        return

    if dict_map.get(user_input) == answer:
        print(f"Correct! {answer['name']} has more followers.")
        score += 1
        print(f"Current score: {score}")
        
    else:
        print(f"Oops! That's wrong.\nFinal score: {score}")
        game_over = True
             
    return score
    

while not game_over:
    if answer:
        A_dict = answer
    else:
        A_dict = selector()
    B_dict = selector()
    selector_checker()
    
    dict_map = {
        "A": A_dict,
        "B": B_dict
    }

    commentator()
    answer_checker()
    answer_declarer()