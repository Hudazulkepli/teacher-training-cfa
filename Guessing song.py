#! /usr/bin/env python3
 
import random as rnd

songlist = {
    'kesetiaan': 'siti sarah',
    'purnama merindu': 'siti nurhaliza',
    'madah berhelah': 'ziana zain',
    'seandainya masih ada cinta': 'dayang nurfaizah',
    'dikir puteri': 'nuraniza idris',
}
 
score = 0;
tries = 3
 
while tries > 0:
    try:
        random_song = rnd.choice(list(songlist.items()))
        intials = []
        for first_letter in random_song[0].split():
            intials.append(first_letter[0].capitalize())
 
        print(f'The intials for the song are {" ".join(intials)} and the artist is {random_song[1].title()}')
        print('Can you guess the song?')
        song = input('>> ')
        if song.lower().strip() == random_song[0].lower().strip():
            print(f'Well done! You have {tries - 1} tries left. Your score is {score + 1}.')
            tries -= 1
            score += 1
            continue
        else:
            print(f'That is incorrect. You have {tries - 1} tries left. Your score is {score}.')
            tries -= 1
            continue
 
        break
    except ValueError as error:
        print(error)