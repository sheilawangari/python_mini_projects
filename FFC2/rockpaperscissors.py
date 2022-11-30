import random 

def play():
    user = input("Whats your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])     # this allows the computer to also choose 

    if user == computer:
        return 'Its a tie' 

    # r > s, s > p, p > r 
    # the computer is the opponent and the user is the player

    if winner(user, computer):
        return 'You won!' 

    return 'You lost!'     # if the computer won then we lost. This runs when both conditions on top are false


def winner(player, opponent):
    # returns true if player wins 

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True 

print(play())