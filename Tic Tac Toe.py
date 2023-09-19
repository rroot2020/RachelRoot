import random
import sys

game=[i for i in range(0,9)]
person, comp = '',''

# Corners, Center and Others, respectively
moves=((1,7,3,9),(5,),(2,4,6,8))
# Winner combinations
winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
# Table
tab=range(1,10)

def print_game():
    x=1
    for i in game:
        end = ' | '
        if x%3 == 0:
            end = ' \n'
            if i != 1: end+='----\n';
        char=' '
        if i in ('X','O'): char=i;
        x+=1
        print(char,end=end)
        
def select_char():
    chars=('X','O')
    if random.randint(0,1) == 0:
        return chars[::-1]
    return chars

def can_move(game, person, move):
    if move in tab and game[move-1] == move-1:
        return True
    return False

def can_win(game, person, move):
    places=[]
    x=0
    for i in game:
        if i == person: places.append(x);
        x+=1
    win=True
    for tup in winners:
        win=True
        for ix in tup:
            if game[ix] != person:
                win=False
                break
        if win == True:
            break
    return win

def make_move(game, person, move, undo=False):
    if can_move(game, person, move):
        game[move-1] = person
        win=can_win(game, person, move)
        if undo:
            game[move-1] = move-1
        return (True, win)
    return (False, False)

# AI goes here
def comp_move():
    move=-1
    # If I can win, others don't matter.
    for i in range(1,10):
        if make_move(game, comp, i, True)[1]:
            move=i
            break
    if move == -1:
        # If player can win, block him.
        for i in range(1,10):
            if make_move(game, person, i, True)[1]:
                move=i
                break
    if move == -1:
        # Otherwise, try to take one of desired places.
        for tup in moves:
            for mv in tup:
                if move == -1 and can_move(game, comp, mv):
                    move=mv
                    break
    return make_move(game, comp, move)

def space_exist():
    return game.count('X') + game.count('O') != 9

person, comp = select_char()
print('Person 1 is [%s] and computer is [%s]' % (person, comp))
result='%%% TIE ! %%%'
while space_exist():
    print_game()
    print('# Choose your number ! [1-9] : ', end='')
    move = int(input())
    moved, won = make_move(game, person, move)
    if not moved:
        print(' >> That is not a valid choice ! Go again !')
        continue
    #
    if won:
        result='*** Woohoo You are a winner winner chicken dinner ! ***'
        break
    elif comp_move()[1]:
        result='=== womp womp ! =='
        break;

print_game()
print(result)