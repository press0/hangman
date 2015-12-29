import random

f = open("hangman.txt",'r')
lister = []
file_data = f.read()
lister = file_data.split('\n')
for index,li in enumerate(lister):
    lister[index] = lister[index].lower()

answer = list(random.choice(lister))


alpabets = tuple(list('abcdefghijklmnopqrstuvwxyz'))
def get_display(answer):
    lister = []
    for char in answer:
        if char in alpabets:
            lister.append('_')
        else:
            lister.append(char)

    return lister
print("WELCOME to HANGMAN GAME")

tries = 7

state = get_display(answer)

print(' '.join(state))

already_guessed = []

while True:
    if tries == 0:
            print("You lost the game. The word was {} ".format(''.join(answer)))
            break
    guess = input("Make a guess : ")

    if guess in already_guessed:
        print("You have already guessed that letter")
        continue
    elif len(guess)>1:
        print("You have to guess a single letter")
        continue
    elif guess not in alpabets:
        print("You have to guess a letter")
    else:
        already_guessed.append(guess)
        if not guess in answer:
            print("Nope {} is not the word try again!!".format(guess))
            print(' '.join(state))
            tries -= 1
            print("You currently have {} tries left ".format(tries))
            continue
        for index,char in enumerate(answer):
            if guess == char:
                state[index] = guess
        print(' '.join(state))

        if state == answer:
            print("You won !! The word was {}".format(''.join(answer)))
            break

input("Press <enter> to exit")


