import time  # import time to sleep some times
import random  # import random to select random objects
# Confugre List Of Objects
Places = ['Real Madrid', 'Barcelona', 'Liverpool']
numbers = ['7', '9', '10', '11']
RealMadrid_position = ['attacker', 'Defender', 'Goal keeper', 'Right wing']
Barcelona_position = ['Right back', 'Left back', 'Midfielder']
Liverpool_position = ['Captin', 'Shadow striker', 'left wing']
Game_Result = ['Goaaaaal', 'No goal']
# End Configuration
# Define Function To print Messages

def GetUserChoise(Input):
    if Choise.lower() == 'Real Madrid'.lower() or Choise.lower() == 'R'.lower() or  Choise == '1':
        return 'Real Madrid'
    elif Choise.lower() == 'Barcelona'.lower() or Choise.lower() == 'B'.lower() or  Choise == '2':
        return 'Barcelona'
    elif Choise.lower() == 'Liverpool'.lower() or Choise.lower() == 'L'.lower() or  Choise == '3':
        return 'Liverpool'
    else:
        return ''
def GetUserMonster(UserChoise):
    if UserChoise == 'Real Madrid':
        print(random.choice(RealMadrid_position))
    if UserChoise == 'Barcelona':
        print(random.choice(Barcelona_position))
    if UserChoise == 'Liverpool':
        print(random.choice(Liverpool_position))
def PrintSleep(msg, seconds):
    print(msg + '\n')
    time.sleep(seconds)
def ChangeWeapon():
    changerequest =input('would you like to change your number\n')
    if changerequest == 'yes':
        numberchoosed=random.choice(numbers)
        print(numberchoosed)
#Game Will Start
RetryGame='y'
while RetryGame=='y':
    PrintSleep('Welcome to the game of adventures fun game ' , 2)
    PrintSleep('Ready!!' , 2)
    PrintSleep('Well we will help you in the game but be careful in your choices it will be the reason for your victory or defeat' , 2)
    name = input('Please Enter Your Name To Start Game \n')
    time.sleep(1)
    print('Please Choose your club Witch want to play in \n')
    time.sleep(1)
    for place in Places:
        print(place)
        time.sleep(1)
    Choise = ''
    while Choise not in Places:
        msg = 'Here are the offers Choose your favorite club to choose Real Madrid write r or Real or 1\n for Barcelona write b or Barcelona or 2 \nfor Liverpool write l or Liverpool or 3\n'
        Choise=input(msg)
        Choise=GetUserChoise(Choise)
    time.sleep(2)
    print('Now you are plying in club ')
    numberchoosed = random.choice(numbers)
    print(numberchoosed)
    ChangeWeapon() 
    print('\nyou now in ' + Choise + ' and your number is ' + numberchoosed)
    time.sleep(1)
    print('now you see fornt of defender ')
    GetUserMonster(Choise)

    time.sleep(2)
    PrintSleep('Use your skill to score a goal' , 2)

    print('you ' + random.choice(Game_Result))
    time.sleep(2)
    print ('Game Over')
    RetryGame=input('Would You Like to try again for yes write y for no write \n')
