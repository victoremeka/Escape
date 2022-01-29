from Core import Secretcode,Choicecheck,Codeinbox,Door,Note,Checklist,Playerdeath

# Your story begins!
print('... \nYou shoot up awake. Something feels different but you can\'t place a finger on it.\nA quick scan of the room you are in confirms your doubts, it\'s not yours.\nThe fact that you were lying on the floor was your first flag but this seems to have comfirmed it.\n')
print('Two eerily identical boxes lie in front of you but you ignore them and head groggily to the door.A keypad warmly greets you once there.\nOn its screen, a blinking message reads "ONE TRY LEFT". It prompts for a four-digit code.\nAs you contemplate this, you remember you passed two identical boxes on you way to the door.\n')
print('You look back to find just that.\nDo you go back or try your luck with the door?\n')
print('1. Go back to the boxes\n2. Try your luck')

breakcount2 = 0
boxcount = 0

for i in range(3):
    prompt = Checklist(None)

    if prompt.isdigit() and 0 < int(prompt) < 3: #choicecheck
        break
    else:
        if i == 2:
            print(Playerdeath)
            quit()
        else:
            print('Enter either 1 or 2')

if prompt == '1': 
    print('\nYou walk back to the boxes and as you examine them, find a note hidden underneath one of them. Do you:')
    print('\n1. Ignore the note\n2. Pick up the note')
    
    while True:
        ch1 = Checklist(None)
        chnum = Choicecheck(ch1,2)
        
        if chnum == '1':

            print('\nBoth boxes stare back at you, devoid of any emotion. You have labelled one "Box A" and the other "Box B".\nWhich do you open?')
            print('\n1.Box A\n2.Box B')

            while True:
                ch2 = Checklist(None)
                chnum2 = Choicecheck(ch2,2)
                chnum2 = int(chnum2)

                if chnum2 == Codeinbox():
                    print('\nYou pick up box',chnum2,', silently hoping it\'s your lucky day. Come to think of it, what day is it anyway?.\nInside, etched on the bottom is a four-digit code:')
                    
                    found = Secretcode(None)
                    print('\n'+found)

                    print('\nElated, you rush back to the door.')
                    print(Secretcode(found))
                    quit()

                elif chnum2 == 0:
                    boxcount += 1
                    if boxcount == 3:
                        print(Playerdeath)
                        quit()
                    else:
                        print('\nEnter either 1 or 2\n')
                        continue
                    
                else:
                    print('You pick up box',chnum2,', silently hoping it\'s your lucky day. Come to think of it, what day is it anyway?.\nAfter thorough inspection, you find nothing. You try to open the other box. It\'s locked.')
                    print('\nWith shaky hands, you pick up the note you had ignored. It reads:\n')
                    Note()
                    print(Door())
                    quit()

        elif chnum == '2':
            print('\nThe note reads:\n')
            Note()
            print(Door())
            break
        
        else:
            breakcount2 += 1
        
            if breakcount2 == 3:
                print(Playerdeath)
                break
            else:
                print('\nEnter either 1 or 2\n')

elif prompt == '2':
    print('\nYou silently hope it\'s your lucky day. Come to think of it, what day is it anyway?\nThe keypad prompts for a four digit code.\n')
    print(Door())