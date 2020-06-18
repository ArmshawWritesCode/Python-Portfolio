#Choose Your Own Adventure Game
import time
print('Welcome to the Not-So-Scary Halloween Walk adventure game!')
print('***********************************************************')
print('You are visiting Magic Kingdom at Disney World in Orlando, Florida.')
print('You go on an evening stroll all alone in a dimly lit part of the park.')
print('You can pick one item to take with you - ')
print('map (m), flashlight (f), chocolate (c), smartphone (p), stuffed animal (s)')
item = input('What do you choose? ')
print('You hear a growling sound.')
choice1 = input('Do you follow the sound? Enter y or n: ')
while not (choice1 == 'y' or choice1 == 'n'):
    choice1 = input("That's not a valid input. Enter y or n: ")
if choice1 =='y':
    print('You keep moving closer to the sound.')
    print('The sound suddenly stops.')
    time.sleep(3)
    print('You are now LOST!! ....')
    time.sleep(3)
    print('You look around for help, but no one is around!')
    direction = input('Which direction do you go? north, south, east or west: ')
    if direction == 'north':
        print('You reach an abandoned treat station.')
        if item == 'm':
            print('You use the map and find your way home.')
            print('CONGRATULATIONS! You won the game.')
        else:
            print('If you had a map, you could find your way back from here.')
            print('---You are still lost. You lost the game.---')
    elif direction == 'south':
        print('You reach a river with a raised bridge.')
        if item == 'p' or item == 'f':
            print('You chose an item that can help you find the lever to lower the bridge.')
            print('You lower the bridge, cross the river and find your way home.')
            print('CONGRATULATIONS! You won the game.')
        else:
            print('If you have a smartphone or flashlight, you cound find the lever to lower the bridge.')
            print('---You are still lost. You lost the game.---')
    elif direction == 'west':
        print('You are walking and trip over a discarded costume.')
        print('You have hurt your foot. You sit down to wait for help.')
        print('This could be a long time. You are still lost.')
        print('---You lost the game.---')
    else:
        print('You reach the edge of Fantasyland. It is still dark.')
        if item == 'c':
            print('You use your chocolate to fuel up.')
            print('You have more walking to do in Tomorrowland.')
            print('CONGRATULATIONS! You are out safely. You won the game.')
        else:
            print('Hold on to your stuffed animal and take a seat.')
            print('Due to tiredness, you give up.')
            print('---You are still lost. You lost the game.')

else:
    print('Good call, you are not taking any risks.')
    print('You start walking back to the entrance.')
    print('You realize that you are LOST!!!')
    print('The sound is behond you and getting louder. You panic!')
    action = input('Do you start running (r), cry for help (c)?: ')
    while action == 'c':
        print('Your cry is unheard.')
        action = input('Do you start running (r), cry for help (c)?: ')
    print('You are running fast. The sound if really loud.')
    print('A woman on an electric scooter comes up behind you.')
    answer = input('She says, "Name my favorite programming language." ')
    if answer.lower() == 'python':
        print('She says, "Yes, Python is my favorite programming language." ')
        print('"If you had some chocolate, I could help you."')
        if item == 'c':
            print('Luckily, you did choose correctly!')
            print('You give her the chocolate.')
            print('She helps you get home.')
            print('CONGRATULATIONS! You won the game.')
        else:
            print('You should have chosen that chocolate.')
            print('She rides away, leaving you alone and lost.')
            print('You lost the game.')
    else:
        print('She did not like your answer.')
        print('She rides away, leaving you lost.')
        print('You lost the game.')
