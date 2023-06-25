import pygame
import pygame_menu
import math
import random
import words


pygame.init()
# Display settings
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Hangman')

# load images 
images = []
for i in range(7):
    images.append(pygame.image.load('hangman'+str(i)+'.png'))

# button variables

RADIUS = 22
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2 )
starty =  400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13)) 
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x,y,chr(A+i),True])

# font
LETTER_FONT = pygame.font.SysFont('comicsans', 30)
WORD_FONT = pygame.font.SysFont('comicsans', 40)
TITLE_FONT = pygame.font.SysFont('comicsans', 50)

# Game variables
hangman_status = 0

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# Words Category
countries = words.countries
capitals = words.capitals
movies = words.movies
tv_seris = words.tv_series
games = words.games
fruits_and_veggies = words.fruits_and_veggies

word = []

def getword():
    # Generate a random word
    for i in games:
        word.append(i.upper())
    
getword()

random_word = random.choice(word)
randomword = str(random_word).replace(" ", "")
guessed = []

# Draw screen and buttons
def draw():
    #screen
    win.fill(WHITE)
    # draw title
    text = TITLE_FONT.render('HELLO',1,BLACK)
    win.blit(text, (50, 50))

    pygame

    #draw word
    display_word = ""
    for letter in randomword:
        if letter in guessed:
            display_word += letter +" "
        else:
            display_word += "_ "
    
    guessed_text = WORD_FONT.render(display_word, 1 , BLACK)
    win.blit(guessed_text,(50,200))
    
    #draw button
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1 ,BLACK)
            win.blit(text, (x - text.get_width()/2 , y - text.get_height()/2))

    win.blit(images[hangman_status], (530,20))
    pygame.display.update()

# final message
def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message,1,BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2 , HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    global hangman_status
    # setup game loop
    FPS = 60
    clock = pygame.time.Clock()
    run = True
    # Running the game
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x , m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x,y,ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x-m_x)**2 + (y-m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in randomword:
                                hangman_status += 1

        draw()
        
        statues = True
        for letter in randomword:
            if letter not in guessed:
                statues = False
                break
        
        if statues == True:
            display_message('YOU WON!')
            display_message(f"The Word '{random_word}'")
            break

        if hangman_status == 6:
            display_message("YOU LOST!")
            display_message(f"The Word '{random_word}'")
            break
        



while True:
    getword()
    main()

pygame.quit()
pygame.display.quit()
