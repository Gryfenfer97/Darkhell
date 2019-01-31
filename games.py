from random import randrange

def rps(choice):
    message = " {0} {1}"
    paper_emo = ":page_facing_up:"
    rock_emo = ":moyai:"
    scissor_emo = ":scissors:"
    if choice == "rock"  or choice == "scissors" or choice == "paper":
        r = randrange(0,3)
        if r == 0: #rock
            if choice == "rock":
                return message.format(rock_emo,"we're square")
            elif choice == "paper":
                return message.format(rock_emo,"you win")
            else:
                return message.format(rock_emo,"you lost")
        elif r == 1: #paper
            if choice == "rock":
                return message.format(paper_emo,"you lost")
            elif choice == "paper":
                return message.format(paper_emo,"we're square")
            else:
                return message.format(paper_emo,"you win")
        if r == 2: #scissors
            if choice == "rock":
                return message.format(scissor_emo,"you win")
            elif choice == "paper":
                return message.format(scissor_emo,"you lost")
            else:
                return message.format(scissor_emo,"we're square")