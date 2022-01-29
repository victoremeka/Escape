
from random import randint


def Secretcode(code): # Contains the 'secret code' to unlocking the door. It also checks to see if it is correct or not
    scode = '55' + eq

    if code == scode:
       return('\nYou gingerly type in the code and hit enter. A mechanical beep follows, and the door opens.\n\nFREEDOM! You shout, and run out, only to realise you are locked in another empty room with three boxes.\nManiacal laughter echoes through the room and a voice speaks. "Welcome to...ESCAPE!"\n')
    elif code is None:
        return(scode)
    else:
        return(Playerdeath)
    
def Choicecheck(choice,num): # Checks to see if player's choice is valid
    if choice.isdigit() and 0 < int(choice) < num+1:
        return choice
    else:
        return 0
    
def Codeinbox():
    return randint(1,2)

def Door(): # Keypad's codecheck
    for i in range(3):
        try:
            luck = input('Enter four-digit code: ')
        except KeyboardInterrupt:
            return('\n' + Playerdeath + 'You pressed Ctrl-c didn\'t ya. *shakes head*\n')
        
        if len(luck) == 4 and luck.isdigit():
            return Secretcode(luck)
        else:
            if i == 2:
                return(Playerdeath)
            else:
                print('Only four-digit numbers are valid.')

def Note():
    print('I looked into my bag and found the most of curious things.\n\nA double digit watch with five buttons and my favourite math operation printed on a piece of paper:')
    print('x² + x = -'+eqcode[2:]+'\n')
    print('~ An excerpt from Kirian Marworths, author of Not An Equation.\n')
    print('"Odd...", you mutter. With no other alternative, you assume it is a riddle of some sort.\nYou head to the keypad on the door. It prompts for a four-digit code.')

def Checklist(var):
    try:
        var = input('Enter choice: ')
        return var
    except KeyboardInterrupt:
        print('\n' + Playerdeath + 'Next time, don\'t Ctrl-c.\n')
        quit()


Playerdeath = '\nA sharp hum is heard and suddenly, darkness fills your vision. \nYour only thought before the world turns dark is sadly, nothing.\n'

eq = str(randint(0,99))

if len(eq) == 1:
    eq = '0'+ eq


eqcode = Secretcode(None)

    
