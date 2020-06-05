import random


# Checking names and points from ratings.txt
name = input('Enter your name: ')
print(f'Hello, {name}')

file = open('rating.txt', 'r+')

list_orig = file.readlines()
list_game = [str(i).strip().split(' ') for i in list_orig]

name_list = [list_game[i][0] for i in range(len(list_game))]
point_list = [int(list_game[i][1]) for i in range(len(list_game))]

names_points = { names:points for (names,points) in zip(name_list, point_list)}
print(names_points)


for entry in list_game:
    if name in entry[0]:
        print(f'Your rating: {entry[1]}')
        break
else:
    file.write(f'\n{name} 0')


# The game itself

options = ['rock','scissors','paper']
my_hand = input()

#rating = names_points[name]

while my_hand != '!exit':
    
    if my_hand in options:
        
        #print(f'User chose: {my_hand}')
        pc_hand = random.choice(options)
        if my_hand == pc_hand:
            print(f'There is a draw ({my_hand})')
            names_points[name] += 50
        if my_hand == 'paper':
            if pc_hand == 'rock':
                print(f'Well done. Computer chose {pc_hand} and failed')
                names_points[name] += 100
            elif pc_hand == 'scissors':
                print(f'Sorry, but computer chose {pc_hand}')
        elif my_hand == 'rock':
            if pc_hand == 'scissors':
                print(f'Well done. Computer chose {pc_hand} and failed')
                names_points[name] += 100
            elif pc_hand == 'paper':
                print(f'Sorry, but computer chose {pc_hand}')
        elif my_hand == 'scissors':
            if pc_hand == 'paper':
                print(f'Well done. Computer chose {pc_hand} and failed')
                names_points[name] += 100
            elif pc_hand == 'rock':
                print(f'Sorry, but computer chose {pc_hand}')
        my_hand = input()

    elif my_hand == '!rating':
        print(f'Your rating: {names_points[name]}')
        my_hand = input()
    else:    
        print("Invalid input")
        my_hand = input()
        
print("Bye!")
     
file.close()