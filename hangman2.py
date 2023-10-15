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
gh = 25
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

idioms = [
    "A BIRD IN THE HAND IS WORTH TWO IN THE BUSH",
    "A BLESSING IN DISGUISE",
    "A DIME A DOZEN",
    "A DROP IN THE BUCKET",
    "A HOT POTATO",
    "A PENNY FOR YOUR THOUGHTS",
    "A SLICE OF THE PIE",
    "A STITCH IN TIME SAVES NINE",
    "A TASTE OF YOUR OWN MEDICINE",
    "AT THE DROP OF A HAT",
    "BACK TO THE DRAWING BOARD",
    "BARKING UP THE WRONG TREE",
    "BEAT AROUND THE BUSH",
    "BEST THING SINCE SLICED BREAD",
    "BETTER LATE THAN NEVER",
    "BITE THE BULLET",
    "BREAK A LEG",
    "CALL IT A DAY",
    "CAT OUT OF THE BAG",
    "CRY OVER SPILLED MILK",
    "CUTTING CORNERS",
    "DON'T CRY OVER SPILLED MILK",
    "DON'T JUDGE A BOOK BY ITS COVER",
    "DON'T PUT ALL YOUR EGGS IN ONE BASKET",
    "DON'T PUT THE CART BEFORE THE HORSE",
    "DON'T THROW STONES IF YOU LIVE IN A GLASS HOUSE",
    "EASIER SAID THAN DONE",
    "FIT AS A FIDDLE",
    "FLYING OFF THE HANDLE",
    "GET A TASTE OF YOUR OWN MEDICINE",
    "GET YOUR ACT TOGETHER",
    "GIVE THE BENEFIT OF THE DOUBT",
    "HIT THE NAIL ON THE HEAD",
    "HIT THE SACK",
    "KEEP AN EYE ON",
    "KICK THE BUCKET",
    "LET THE CAT OUT OF THE BAG",
    "MIND OVER MATTER",
    "NO PAIN, NO GAIN",
    "ON THE BALL",
    "RAINING CATS AND DOGS",
    "SIT ON THE FENCE",
    "SPEAK OF THE DEVIL",
    "TAKE IT WITH A GRAIN OF SALT",
    "THE BALL IS IN YOUR COURT",
    "THE BEST OF BOTH WORLDS",
    "THE ELEPHANT IN THE ROOM",
    "THROW IN THE TOWEL",
    "WALK ON EGGSHELLS",
    "A CHIP ON YOUR SHOULDER",
    "A DARK HORSE",
    "A DROP IN THE BUCKET",
    "A HOUSE OF CARDS",
    "A LITTLE BIRD TOLD ME",
    "A PENNY FOR YOUR THOUGHTS",
    "ALL THUMBS",
    "APPLE OF MY EYE",
    "BACK TO SQUARE ONE",
    "BETWEEN A ROCK AND A HARD PLACE",
    "BURNING THE MIDNIGHT OIL",
    "BURY THE HATCHET",
    "CALL A SPADE A SPADE",
    "CROSS THAT BRIDGE WHEN YOU COME TO IT",
    "DON'T PUT ALL YOUR EGGS IN ONE BASKET",
    "FISH OUT OF WATER",
    "HEAD OVER HEELS",
    "HIT THE NAIL ON THE HEAD",
    "HIT THE HAY",
    "IN THE NICK OF TIME",
    "IT TAKES TWO TO TANGO",
    "JUMP ON THE BANDWAGON",
    "KICK THE BUCKET",
    "LAST STRAW",
    "MAKE A LONG STORY SHORT",
    "ON CLOUD NINE",
    "PIE IN THE SKY",
    "PULL A RABBIT OUT OF THE HAT",
    "RAKE SOMEONE OVER THE COALS",
    "SPILL THE BEANS",
    "THROW IN THE TOWEL",
    "TURN OVER A NEW LEAF",
    "WATER UNDER THE BRIDGE",
    "WEAR YOUR HEART ON YOUR SLEEVE",
]

books = [
    "IT WAS THE BEST OF TIMES, IT WAS THE WORST OF TIMES",
    "IN MY YOUNGER AND MORE VULNERABLE YEARS, MY FATHER GAVE ME SOME ADVICE",
    "MANY YEARS LATER, AS HE FACED THE FIRING SQUAD, COLONEL AURELIANO BUENDÍA WAS TO REMEMBER THAT DISTANT AFTERNOON",
    "THERE WAS A BOY CALLED EUSTACE CLARENCE SCRUBB, AND HE ALMOST DESERVED IT",
    "THERE WAS NO POSSIBILITY OF TAKING A WALK THAT DAY",
    "WHEN I WROTE THE FOLLOWING PAGES, OR RATHER THE BULK OF THEM, I LIVED ALONE, IN THE WOODS, A MILE FROM ANY NEIGHBOR",
    "IT IS A TRUTH UNIVERSALLY ACKNOWLEDGED, THAT A SINGLE MAN IN POSSESSION OF A GOOD FORTUNE, MUST BE IN WANT OF A WIFE",
    "RIVERWINDS KNOWS YOU. IT HAS KNOWN YOU A LONG TIME. SINCE YOU WERE A CHILD",
    "A SCREAMING COMES ACROSS THE SKY",
    "THERE WAS A HAND IN THE DARK, AND IT HELD A KNIFE",
    "THE DELTA, A VAST, BLACK OCEAN, WITH THE OLD FLOATING HOME MOVING ON IT",
    "THERE IS NO ELOQUENCE WHERE THERE IS NO TRUTH",
    "I AM AN INVISIBLE MAN",
    "THERE IS A CURTAIN, THIN AS GOSIMER, CLEAR AS GLASS, STRONG AS IRON, THAT SEPARATES THE FACES FROM THE HEARTS",
    "THERE WAS A BOY NAMED EGLANTINE, WHOSE MOTHER CALLED HIM TINE"
    "BILBO BAGGINS WAS A HOBBIT WHO LIVED IN HIS HOBBIT-HOLE AND NEVER WENT FOR ADVENTURES",
    "IT IS A SAD THING, NOT TO HAVE FRIENDS, BUT IT IS EVEN SADDER NOT TO HAVE ENEMIES",
    "I AM BY BIRTH A GENEVESSE; AND MY FAMILY IS ONE OF THE MOST DISTINGUISHED OF THAT REPUBLIC",
    "MOTHER DIED TODAY. OR MAYBE YESTERDAY, I CAN'T BE SURE",
    "MY LIFE BEGAN IN A HOLE, IN THE GROUND"
    "MARIUS' FRIEND, CURFEW, WAS NOT A PERSON; IT WAS A THING. IN THE AWFUL HIEROGLYPHS OF THE TOILET-VAULTS"
    "I'VE WATCHED THROUGH HIS EYES, I'VE LISTENED THROUGH HIS EARS, AND TELL YOU HE'S THE ONE"
    "WHAT'S IT GOING TO BE THEN, EH?"
    "IN A HOLE IN THE GROUND THERE LIVED A HOBBIT",
    "AFTER THE TURQUOISE COLOR OF THE SEA AND OF THE LILIES AND THE LACE FRILL OF THE WAVES, AFTER THE COLOR OF THE SEA AND THE COLOR OF THE FLOWERS, AND THE COLOR OF THE LACE, TURQUOISE, THE COLOR OF THE SEA, AND LILIES"
    "THERE WAS NO POSSIBILITY OF TAKING A WALK THAT DAY"
    "A FROG CAME TO VISIT AND STAYED TOO LONG"
    "THERE WAS A HAND IN THE DARK, AND IT HELD A KNIFE"
    "RIVERRUN, PAST EVE AND ADAM'S, FROM SWERVE OF SHORE TO BEND OF BAY"
    "THERE IS NO ELOQUENCE WHERE THERE IS NO TRUTH"
    "I AM AN INVISIBLE MAN"
    "THERE IS A CURTAIN, THIN AS GOSIMER, CLEAR AS GLASS, STRONG AS IRON, THAT SEPARATES THE FACES FROM THE HEARTS"
    "THERE WAS A BOY NAMED EGLANTINE, WHOSE MOTHER CALLED HIM TINE"
    "MOTHER DIED TODAY. OR MAYBE YESTERDAY, I CAN'T BE SURE"
    "MY LIFE BEGAN IN A HOLE, IN THE GROUND"
    "MARIUS' FRIEND, CURFEW, WAS NOT A PERSON; IT WAS A THING. IN THE AWFUL HIEROGLYPHS OF THE TOILET-VAULTS"
    "I'VE WATCHED THROUGH HIS EYES, I'VE LISTENED THROUGH HIS EARS, AND TELL YOU HE'S THE ONE"
    "WHAT'S IT GOING TO BE THEN, EH?"
    "IN A HOLE IN THE GROUND THERE LIVED A HOBBIT"
    "AFTER THE TURQUOISE COLOR OF THE SEA AND OF THE LILIES AND THE LACE FRILL OF THE WAVES, AFTER THE COLOR OF THE SEA AND THE COLOR OF THE FLOWERS, AND THE COLOR OF THE LACE, TURQUOISE, THE COLOR OF THE SEA, AND LILIES"
    "THERE WAS NO POSSIBILITY OF TAKING A WALK THAT DAY"
    "A FROG CAME TO VISIT AND STAYED TOO LONG"
    "THERE WAS A HAND IN THE DARK, AND IT HELD A KNIFE"
    "RIVERRUN, PAST EVE AND ADAM'S, FROM SWERVE OF SHORE TO BEND OF BAY"
    "THERE IS NO ELOQUENCE WHERE THERE IS NO TRUTH"
    "I AM AN INVISIBLE MAN"
    "THERE IS A CURTAIN, THIN AS GOSIMER, CLEAR AS GLASS, STRONG AS IRON, THAT SEPARATES THE FACES FROM THE HEARTS"
    "THERE WAS A BOY NAMED EGLANTINE, WHOSE MOTHER CALLED HIM TINE"
    "MOTHER DIED TODAY. OR MAYBE YESTERDAY, I CAN'T BE SURE"
    "MY LIFE BEGAN IN A HOLE, IN THE GROUND"
    "MARIUS' FRIEND, CURFEW, WAS NOT A PERSON; IT WAS A THING. IN THE AWFUL HIEROGLYPHS OF THE TOILET-VAULTS"
    "I'VE WATCHED THROUGH HIS EYES, I'VE LISTENED THROUGH HIS EARS, AND TELL YOU HE'S THE ONE"
    "WHAT'S IT GOING TO BE THEN, EH?"
    "IN A HOLE IN THE GROUND THERE LIVED A HOBBIT"
    "AFTER THE TURQUOISE COLOR OF THE SEA AND OF THE LILIES AND THE LACE FRILL OF THE WAVES, AFTER THE COLOR OF THE SEA AND THE COLOR OF THE FLOWERS, AND THE COLOR OF THE LACE, TURQUOISE, THE COLOR OF THE SEA, AND LILIES"
]

quote = [
    "TO BE YOURSELF IN A WORLD THAT IS CONSTANTLY TRYING TO MAKE YOU SOMETHING ELSE IS THE GREATEST ACCOMPLISHMENT.",
    "IN THREE WORDS I CAN SUM UP EVERYTHING I'VE LEARNED ABOUT LIFE: IT GOES ON.",
    "NOTHING CAN DIM THE LIGHT WHICH SHINES FROM WITHIN.",
    "THE ONLY WAY TO DO GREAT WORK IS TO LOVE WHAT YOU DO.",
    "THERE IS NO GREATER AGONY THAN BEARING AN UNTOLD STORY INSIDE YOU.",
    "THE ONLY THING WE HAVE TO FEAR IS FEAR ITSELF.",
    "LIFE IS REALLY SIMPLE, BUT WE INSIST ON MAKING IT COMPLICATED.",
    "TWO THINGS ARE INFINITE: THE UNIVERSE AND HUMAN STUPIDITY; AND I'M NOT SURE ABOUT THE UNIVERSE.",
    "TO THE WELL-ORGANIZED MIND, DEATH IS BUT THE NEXT GREAT ADVENTURE.",
    "TO THE BATMOBILE!",
    "THERE IS NO CHARM EQUAL TO TENDERNESS OF HEART.",
    "ALL THAT WE SEE OR SEEM IS BUT A DREAM WITHIN A DREAM.",
    "TO LIVE IS THE RAREST THING IN THE WORLD. MOST PEOPLE EXIST, THAT IS ALL.",
    "THE BEST WAY TO PREDICT THE FUTURE IS TO CREATE IT.",
    "IT WAS THE BEST OF TIMES, IT WAS THE WORST OF TIMES.",
    "IF YOU WANT TO KNOW WHAT A MAN'S LIKE, TAKE A GOOD LOOK AT HOW HE TREATS HIS INFERIORS.",
    "IN THE END, WE WILL REMEMBER NOT THE WORDS OF OUR ENEMIES, BUT THE SILENCE OF OUR FRIENDS.",
    "GREAT THINGS ARE DONE BY A SERIES OF SMALL THINGS BROUGHT TOGETHER.",
    "BREVITY IS THE SOUL OF WIT.",
    "TO BE OR NOT TO BE, THAT IS THE QUESTION.",
    "IT IS A TRUTH UNIVERSALLY ACKNOWLEDGED, THAT A SINGLE MAN IN POSSESSION OF A GOOD FORTUNE, MUST BE IN WANT OF A WIFE.",
    "THE SKY ABOVE THE PORT WAS THE COLOR OF TELEVISION, TUNED TO A DEAD CHANNEL.",
    "WE ARE ALL FOOLS IN LOVE.",
    "TO LIVE IS THE RAREST THING IN THE WORLD. MOST PEOPLE EXIST, THAT IS ALL.",
    "IF YOU CAN DREAM IT, YOU CAN DO IT.",
    "THE BEST WAY TO PREDICT THE FUTURE IS TO CREATE IT.",
    "ALL YOU NEED IS LOVE.",
    "TO BE OR NOT TO BE, THAT IS THE QUESTION.",
    "THE BEST WAY TO PREDICT THE FUTURE IS TO CREATE IT.",
    "IT WAS THE BEST OF TIMES, IT WAS THE WORST OF TIMES.",
    "IF YOU WANT TO KNOW WHAT A MAN'S LIKE, TAKE A GOOD LOOK AT HOW HE TREATS HIS INFERIORS.",
    "IN THE END, WE WILL REMEMBER NOT THE WORDS OF OUR ENEMIES, BUT THE SILENCE OF OUR FRIENDS.",
    "GREAT THINGS ARE DONE BY A SERIES OF SMALL THINGS BROUGHT TOGETHER.",
    "BREVITY IS THE SOUL OF WIT.",
    "TO BE OR NOT TO BE, THAT IS THE QUESTION.",
    "IT IS A TRUTH UNIVERSALLY ACKNOWLEDGED, THAT A SINGLE MAN IN POSSESSION OF A GOOD FORTUNE, MUST BE IN WANT OF A WIFE.",
    "THE SKY ABOVE THE PORT WAS THE COLOR OF TELEVISION, TUNED TO A DEAD CHANNEL.",
    "WE ARE ALL FOOLS IN LOVE.",
    "TO LIVE IS THE RAREST THING IN THE WORLD. MOST PEOPLE EXIST, THAT IS ALL.",
    "IF YOU CAN DREAM IT, YOU CAN DO IT.",
    "WHEN YOU HAVE ELIMINATED THE IMPOSSIBLE, WHATEVER REMAINS, HOWEVER IMPROBABLE, MUST BE THE TRUTH.",
    "THE SECRET OF GETTING AHEAD IS GETTING STARTED.",
    "DO NOT GO GENTLE INTO THAT GOOD NIGHT.",
    "THE ONLY WAY TO DO GREAT WORK IS TO LOVE WHAT YOU DO.",
    "AND, WHEN YOU WANT SOMETHING, ALL THE UNIVERSE CONSPIRES IN HELPING YOU TO ACHIEVE IT.",
    "HAPPINESS CAN BE FOUND EVEN IN THE DARKEST OF TIMES IF ONE ONLY REMEMBERS TO TURN ON THE LIGHT.",
    "THE NIGHT IS DARK AND FULL OF TERRORS.",
    "MAY THE FORCE BE WITH YOU.",
    "IN A HOLE IN THE GROUND THERE LIVED A HOBBIT.",
    "THE FIRST RULE OF FIGHT CLUB IS: YOU DO NOT TALK ABOUT FIGHT CLUB.",
    "TO BE OR NOT TO BE, THAT IS THE QUESTION.",
    "TO LIVE IS THE RAREST THING IN THE WORLD. MOST PEOPLE EXIST, THAT IS ALL.",
    "LIFE IS REALLY SIMPLE, BUT WE INSIST ON MAKING IT COMPLICATED.",
    "THE ONLY WAY TO DO GREAT WORK IS TO LOVE WHAT YOU DO.",
    "TO THE WELL-ORGANIZED MIND, DEATH IS BUT THE NEXT GREAT ADVENTURE.",
    "TWO THINGS ARE INFINITE: THE UNIVERSE AND HUMAN STUPIDITY; AND I'M NOT SURE ABOUT THE UNIVERSE.",
    "TO THE BATMOBILE!",
]

idioms = set(idioms)
books = set(books)
quote = set(quote)

idioms = list(idioms)
books = list(books)
quote = list(quote)

# colors
BLACK = (255,255,255)
WHITE = (0,0,0)


def draw():
    global beg
    global now
    global gh
    global hangman_status
    global word
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
    print('WORD -> ', word)
    
    display_word = ""
    for letter in word:
        if letter == ' ':
            display_word += ' '
        elif letter in guessed:
            display_word += letter + ""
        else:
            display_word += "_"
    print('DISPLAY -> ', display_word)
    wo = display_word.split(' ')
    print(len(wo))
    print(len(wo[0]))
    print(wo[0])
    for j in range(len(wo)):
        po = ''
        for o in wo[j]:
            if o == '_':
                po += o + ' '
            else:
                po += o
            
        wo[j] = po
    print(wo)
    y = 200
    while True:
        if len(wo)==0:
            break
        s = 0
        if (len(wo[0])>25):
            print('Length ragequit')
            pygame.quit()
        for i in range(len(wo)):
            s+=len(wo[i])
            if s > 30:
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

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
    if hangman_status > 8:
        hangman_status = 8
    win.blit(images[hangman_status], (50, 50))
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
                    if event.key == pygame.K_b:
                        word = random.choice(books)
                        books.remove(word)
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
                            wo = []
                            word = ''
                            a = False
                            b = True
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
