import random 

from wordlist import easy_wordlist, medium_wordlist, hard_wordlist

DIFFICULTY_LEVEL = "easy"

def hangman(tries):
    """
    list of symbolic representation of losing the tries/wrong attempts(HANGMAN GAME)
    """
    the_stages = [
        """
        #hangman body
                _______
                |     |
                |    ___
                |     O
                |    /|\ 
                |     | 
                |    / \ 
                |  _/   \_
                |______________

        #hangman feet
        _______
        |     |
        |     O
        |    /|\ 
        |     | 
        |    / \ 
        |  _/   \_
        |______________
        
        #hangman right leg
        _______
        |     |
        |     O
        |    /|\ 
        |     | 
        |    / \ 
        |   /   \ 
        |______________
        #hangman left foot
        _______
        |     |
        |     O
        |    /|\ 
        |     | 
        |    / 
        |   /   
        |______________
        #hangman right hand
        _______
        |     |
        |     O
        |    /|\ 
        |     | 
        |    
        |     
        |______________
        #hangman left hand
        _______
        |     |
        |     O
        |    /| 
        |     | 
        |     
        |      
        |______________
        #hangman torso
        _______
        |     |
        |     O
        |     | 
        |     |
        |    
        |   
        |______________
        #hangman head
        _______
        |     |
        |     O
        |______________
        #hangman zero
        _______
        |     |
        |     
        |______________

        """
    ]
    return the_stages(tries)

def get_word():
     """
    easy_wordlist (list): list of words (strings) - for easy difficulty level
    medium_wordlist (list): list of words (strings) - for medium difficulty level
    hard_wordlist (list): list of words (strings) - for hard difficulty level

    Returns a word from wordlist at random
    """

    if DIFFICULTY_LEVEL == "easy":
        word = random.choice(easy_wordlist)
    elif DIFFICULTY_LEVEL == "medium":
        word = random.choice(medium_wordlist)
    elif DIFFICULTY_LEVEL == "hard":
        word = random.choice(hard_wordlist)
    else:
        word = random.choice(easy_wordlist)
    return word.upper()

def choose_difficulty():
    global DIFFICULTY_LEVEL
    DIFFICULTY_LEVEL = input("Choose your difficulty").lower()
    if DIFFICULTY_LEVEL == "easy":
        return(
            8
        )
    elif DIFFICULTY_LEVEL == "medium":
        return(
            6
        )
    elif DIFFICULTY_LEVEL =="hard":
        return(
            6
        )
    else:
        print("invalid level")
        return 6
    


