#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 05:34:46 2023

@author: dsarkar
"""

import pygame
import math
import random
import time
guessed = []
gh = 30
# setup display
pygame.init()
WIDTH, HEIGHT = 1920, 1080
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman!")

# button variables
RADIUS = 30
GAP = 20
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 800
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)
T_FONT = pygame.font.SysFont('comicsans', 30)

# load images.
images = []
for i in range(9):
    image = pygame.image.load("hang" + str(i) + ".jpg")
    images.append(image)

# game variables
hangman_status = 0
words = ["THIS IS A TEST OF HOW LONG THE WORD CAN BE FOR THIS THING"]

idioms = ['CRY OVER SPILLED MILK',"DON'T PUT ALL YOUR EGGS IN ONE BASKET","HIT THE NAIL ON THE HEAD",\
          "IT'S RAINING CATS AND DOGS", "JUMP ON THE BANDWAGON", "LET THE CAT OUT OF THE BAG",\
          "READ BETWEEN THE LINES","TAKE WITH A GRAIN OF SALT","THE BALL IS IN YOUR COURT", \
              "YOU CAN'T MAKE AN OMELETTE WITHOUT BREAKING EGGS", "A PENNY FOR YOUR THOUGHTS", \
                  "HIT THE NAIL ON THE HEAD", "BURNING THE MIDNIGHT OIL", "GIVE THE BENEFIT OF THE DOUBT",\
                      "A BURNT CHILD DREADS THE FIRE", "QUIT COLD TURKEY", "NO PAIN, NO GAIN", "ACTIONS SPEAK LOUDER THAN WORDS"]


book = ["IT WAS THE BEST OF TIMES, IT WAS THE WORST OF TIMES.",\
        "LOLITA, LIGHT OF MY LIFE, FIRE OF MY LOINS",\
            "IT WAS A BRIGHT COLD DAY IN APRIL, AND THE CLOCKS WERE STRIKING THIRTEEN.", \
                "IF YOU REALLY WANT TO HEAR ABOUT IT, THE FIRST THING YOU'LL PROBABLY WANT TO KNOW IS WHERE I WAS BORN.", \
                    "IN A HOLE IN THE GROUND, THERE LIVED A HOBBIT.", \
                        "THE SKY ABOVE THE PORT WAS THE COLOR OF TELEVISION, TUNED TO A DEAD CHANNEL.", \
                            "THERE WAS A BOY CALLED EUSTACE CLARENCE SCRUBB, AND HE ALMOST DESERVED IT.", \
                                "IT WAS THE DAY MY GRANDMOTHER EXPLODED.", \
                                    "IN MY YOUNGER AND MORE VULNERABLE YEARS, MY FATHER GAVE ME SOME ADVICE THAT I'VE BEEN TURNING OVER IN MY MIND EVER SINCE.", \
                                        "THE SUN SHONE, HAVING NO ALTERNATIVE, ON NOTHING NEW", \
                                            "IT IS A TRUTH UNIVERSALLY ACKNOWLEDGED, THAT A SINGLE MAN IN POSSESSION OF A GOOD FORTUNE, MUST BE IN WANT OF A WIFE."]
quote = ["TO BE OR NOT TO BE, THAT IS THE QUESTION.",\
         "THE ONLY WAY TO DEAL WITH ALL THE BAD THINGS IN LIFE IS TO TRY TO DO SOMETHING GOOD.", \
             "TO LIVE IS THE RAREST THING IN THE WORLD. MOST PEOPLE EXIST, THAT IS ALL.", \
                 "THE BEST WAY TO PREDICT THE FUTURE IS TO CREATE IT.", \
                     "ALL THAT IS GOLD DOES NOT GLITTER, NOT ALL THOSE WHO WANDER ARE LOST.", \
                         "KEEP YOUR FRIENDS CLOSE AND YOUR ENEMIES CLOSER.", \
                             "IN THREE WORDS I CAN SUM UP EVERYTHING I'VE LEARNED ABOUT LIFE: IT GOES ON.", \
                                 "ALL HAPPY FAMILIES ARE ALIKE; EACH UNHAPPY FAMILY IS UNHAPPY IN ITS OWN WAY.", \
                                     "WHATEVER OUR SOULS ARE MADE OF, HIS AND MINE ARE THE SAME.", \
                                         "ALL ANIMALS ARE EQUAL, BUT SOME ANIMALS ARE MORE EQUAL THAN OTHERS.", \
                                             "IT DOES NOT DO TO DWELL ON DREAMS AND FORGET TO LIVE.", \
                                                 "THE ONLY THING WE HAVE TO FEAR IS FEAR ITSELF."]
'''
word = random.choice(words)
guessed = []
for i in word:
    if i in " !@#$%^&*()_+-=[]\{}|;':<>?,./":
        guessed.append(i)
    else:
        pass
'''

# colors
BLACK = (255,255,255)
WHITE = (0,0,0)


def draw():
    global beg
    global now
    global gh
    global hangman_status
    win.fill(WHITE)
    now = time.time()
    #print('TIME -> ',now)
    ti = str(round(gh - round(abs(beg-now),2),2))
    text = WORD_FONT.render(ti, 1, BLACK)
    win.blit(text, (1750,30))

    # draw title
    text = TITLE_FONT.render("Hangman!", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + ""
        else:
            display_word += "_"
    wo = display_word.split(' ')
    for j in range(len(wo)):
        po = ''
        for o in wo[j]:
            if o == '_':
                po += o + ' '
            else:
                po += o
            
        wo[j] = po
    print('DISPLAY -> ',display_word)
    print(wo)
    y = 200
    while True:
        if len(wo)==0:
            break
        s = 0
        print('LEN ->', len(wo[0]))
        if (len(wo[0])>50):
            pygame.quit()
        for i in range(len(wo)):
            s+=len(wo[i])
            if s > 55:
                la = i - 1
                break
            la = i
        st = ''
        for i in range(la+1):
            st += wo[i]+'  '
        wo = wo[la+1:]
        print(st)
        text = WORD_FONT.render(st, 1, BLACK)
        win.blit(text, (600, y))
        y += 55
     
    '''                  
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (600, 200))
    '''
    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
    if hangman_status > 8:
        hangman_status = 8
    win.blit(images[hangman_status], (100, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    text = T_FONT.render(word, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2 + 75))
    pygame.display.update()
    pygame.time.delay(3000)

start = 0
b = True
def main():
    global hangman_status
    global run
    global start
    global beg
    global word
    global idioms
    global book
    global quote
    global guessed
    global gh
    global letters
    global b

    FPS = 200
    clock = pygame.time.Clock()
    run = True

    clock.tick(FPS)
    pygame.display.update()
    
    while b:
        if start == 0:
            message = 'PRESS ANY KEY TO START!'
            win.fill(WHITE)
            text = WORD_FONT.render(message, 1, BLACK)
            win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
            message = 'I - Idioms, B - Opening Lines, Q - Quotes'
            win.fill(WHITE)
            text = T_FONT.render(message, 1, BLACK)
            win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2 + 40))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    start = 1
                    word = "NO"
                    if event.key == pygame.K_b:
                        word = random.choice(book)
                        book.remove(word)
                        guessed = []
                        for i in word:
                            if i in " !@#$%^&*()_+-=[]\{}|;':<>?,./":
                                guessed.append(i)
                            else:
                                pass
                    if event.key == pygame.K_q:
                        word = random.choice(quote)
                        quote.remove(word)
                        guessed = []
                        for i in word:
                            if i in " !@#$%^&*()_+-=[]\{}|;':<>?,./":
                                guessed.append(i)
                            else:
                                pass
                    if event.key == pygame.K_i:
                        word = random.choice(idioms)
                        idioms.remove(word)
                        guessed = []
                        for i in word:
                            if i in " !@#$%^&*()_+-=[]\{}|;':<>?,./":
                                guessed.append(i)
                            else:
                                pass
                    beg = time.time()
                    b = False

    if start == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
            if event.type == pygame.KEYDOWN:
                K = int(str(event.key))
                print('KEY PRESSED -> ', K)
                if not (123 > K > 96):
                    K = 0
                k = str(chr(K)).upper()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        if k == ltr:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1

            draw()
            
            won = True
            for letter in word:
                if letter not in guessed:
                    won = False
                    break
            
            if won:
                display_message("You WON!")
                a = True
                while a:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            hangman_status = 0
                            start = 0
                            a = False
                            b = True
                            guessed = []
                            for i in range(26):
                                x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
                                y = starty + ((i // 13) * (GAP + RADIUS * 2))
                                letters.append([x, y, chr(A + i), True])
                            pygame.display.update()
                            pygame.time.delay(1000)
                            break
    
            if hangman_status >7 or (gh - abs(now-beg) < 0):
                display_message("You LOST!")
                print('loose')
                a = True
                while a:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            hangman_status = 0
                            start = 0
                            a = False
                            b = True
                            guessed = []
                            for i in range(26):
                                x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
                                y = starty + ((i // 13) * (GAP + RADIUS * 2))
                                letters.append([x, y, chr(A + i), True])
                            pygame.display.update()
                            pygame.time.delay(1000)
                            break

run = True
while run:
    main()
    
pygame.quit()