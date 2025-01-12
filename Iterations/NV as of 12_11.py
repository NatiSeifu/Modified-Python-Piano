# NATI SEIFU
# FINAL PROJECT FOR CS 155
# A MODIFIED PYTHON PIANO
# ABOUT 80% of this code was obtained from (https://www.youtube.com/watch?v=47c_1wOa2so&list=WL&index=11&t=1069s)
# You can check out what his program is like by opening one of the Step files in the document and looking at it against mine.
# I put MA ("My addition") on some dispersed code to indicate that it was added by me


# WHAT    I   LEARNED


# I learned a lot of things about pygame. The code I sourced this from is written very cleanly in pygame.
# Using blit, how to specifcally use mathematics to make things align perfectly, using loops and functions efficiently...
#..., using rect, importing from local files, the applications of "__main__". With time and effort, I see that it is manageable to learn
#...a complicated piece of code and understand it. It seemed like a hefty task that I wouldn't manage at first but after spending time on
#...it, I realized that I could actually accomplish the things that I wanted. I also had some conversations with the creator about his code
#...and how to use it.





#POSSIBLE FUTURE ADDITIONS
    # Different colors for different modes?
    # Creating popups to take user input on what they want to hear
    # Creating a database with different moods
    # DISPLAYING "PLAYED SOUNDS" as they play as opposed to after




from random import randint #MA
import pygame
import piano_lists as pl
from pygame import mixer
import time

pygame.init()
pygame.mixer.set_num_channels(50)

font = pygame.font.Font('assets/Terserah.ttf', 48)
medium_font = pygame.font.Font('assets/Terserah.ttf', 28)
small_font = pygame.font.Font('assets/Terserah.ttf', 16)
real_small_font = pygame.font.Font('assets/Terserah.ttf', 10)
nati_font = pygame.font.Font('assets/ChrustyRock.ttf', 15)
nati2_font = pygame.font.Font('assets/ChrustyRock.ttf', 13)
fps = 60
timer = pygame.time.Clock()
WIDTH = 52 * 35
HEIGHT = 400
screen = pygame.display.set_mode([WIDTH, HEIGHT])
white_sounds = []
black_sounds = []
active_whites = []
active_blacks = []

piano_sounds = [] #defined piano_sounds as an empty list as done above #MA
delay = 0.7 #delay between notes #MA
left_oct = 4
right_oct = 5

left_hand = pl.left_hand
right_hand = pl.right_hand
piano_notes = pl.piano_notes 
piano_labels = pl.piano_labels #needed to add this to accomodate the files named as flats instead of sharps #MA
white_notes = pl.white_notes
black_notes = pl.black_notes
black_labels = pl.black_labels

rand_color = randint(221,254)
KEY_COLOR = (245, rand_color, 245)



for i in range(len(white_notes)):
    white_sounds.append(mixer.Sound(f'assets\\notes\\{white_notes[i]}.wav'))

for i in range(len(black_notes)):
    black_sounds.append(mixer.Sound(f'assets\\notes\\{black_notes[i]}.wav'))

for i in range(len(piano_notes)): #appending all the piano sounds to a list called piano_sounds similar to how it is done on the lines above #MA
    piano_sounds.append(mixer.Sound(f'assets\\notes\\{piano_notes[i]}.wav'))

pygame.display.set_caption("Nati's Version of Python Piano")


def draw_piano(whites, blacks):
    rand_color = randint(221,254) #MA
    white_rects = []
    for i in range(52):
        rect = pygame.draw.rect(screen, KEY_COLOR, [i * 35, HEIGHT - 300, 35, 300], 0, 2) #The rectangles that represent the keys
        white_rects.append(rect)
        #print ("Color is", KEY_COLOR)
        pygame.draw.rect(screen, 'black', [i * 35, HEIGHT - 300, 35, 300], 2, 2) #The outlines for these rectangles
        key_label = small_font.render(white_notes[i], True, 'black') #Configuring the font
        screen.blit(key_label, (i * 35 + 3, HEIGHT - 20)) #Printing these fonts on the keys
    skip_count = 0
    last_skip = 2
    skip_track = 2
    black_rects = []
    for i in range(36):
        rect = pygame.draw.rect(screen, 'black', [23 + (i * 35) + (skip_count * 35), HEIGHT - 300, 24, 200], 0, 2)
        for q in range(len(blacks)):
            #print('This is', len(blacks))
            if blacks[q][0] == i:
                if blacks[q][1] > 0:
                    pygame.draw.rect(screen, 'purple', [23 + (i * 35) + (skip_count * 35), HEIGHT - 300, 24, 200], 3, 2)
                    blacks[q][1] -= 1

        key_label = real_small_font.render(black_labels[i], True, 'white')
        screen.blit(key_label, (25 + (i * 35) + (skip_count * 35), HEIGHT - 120))
        black_rects.append(rect)
        skip_track += 1
        if last_skip == 2 and skip_track == 3:
            last_skip = 3
            skip_track = 0
            skip_count += 1
        elif last_skip == 3 and skip_track == 2:
            last_skip = 2
            skip_track = 0
            skip_count += 1

    for i in range(len(whites)):
        if whites[i][1] > 0:
            j = whites[i][0]
            pygame.draw.rect(screen, 'pink', [j * 35, HEIGHT - 100, 35, 100], 3, 2)
            whites[i][1] -= 1 #This makes the pink last for as long as the fps or less

    return white_rects, black_rects, whites, blacks
    #return white_rects, black_rects


def draw_hands(rightOct, leftOct, rightHand, leftHand): #draws where the hands should be placed
    # left hand
    pygame.draw.rect(screen, 'dark gray', [(leftOct * 245) - 175, HEIGHT - 60, 245, 30], 0, 4)
    pygame.draw.rect(screen, 'black', [(leftOct * 245) - 175, HEIGHT - 60, 245, 30], 4, 4)
    text = small_font.render(leftHand[0], True, 'white')
    screen.blit(text, ((leftOct * 245) - 165, HEIGHT - 55))
    text = small_font.render(leftHand[2], True, 'white')
    screen.blit(text, ((leftOct * 245) - 130, HEIGHT - 55))
    text = small_font.render(leftHand[4], True, 'white')
    screen.blit(text, ((leftOct * 245) - 95, HEIGHT - 55))
    text = small_font.render(leftHand[5], True, 'white')
    screen.blit(text, ((leftOct * 245) - 60, HEIGHT - 55))
    text = small_font.render(leftHand[7], True, 'white')
    screen.blit(text, ((leftOct * 245) - 25, HEIGHT - 55))
    text = small_font.render(leftHand[9], True, 'white')
    screen.blit(text, ((leftOct * 245) + 10, HEIGHT - 55))
    text = small_font.render(leftHand[11], True, 'white')
    screen.blit(text, ((leftOct * 245) + 45, HEIGHT - 55))
    text = small_font.render(leftHand[1], True, 'black')
    screen.blit(text, ((leftOct * 245) - 148, HEIGHT - 55))
    text = small_font.render(leftHand[3], True, 'black')
    screen.blit(text, ((leftOct * 245) - 113, HEIGHT - 55))
    text = small_font.render(leftHand[6], True, 'black')
    screen.blit(text, ((leftOct * 245) - 43, HEIGHT - 55))
    text = small_font.render(leftHand[8], True, 'black')
    screen.blit(text, ((leftOct * 245) - 8, HEIGHT - 55))
    text = small_font.render(leftHand[10], True, 'black')
    screen.blit(text, ((leftOct * 245) + 27, HEIGHT - 55))
    # right hand
    pygame.draw.rect(screen, 'dark gray', [(rightOct * 245) - 175, HEIGHT - 60, 245, 30], 0, 4)
    pygame.draw.rect(screen, 'black', [(rightOct * 245) - 175, HEIGHT - 60, 245, 30], 4, 4)
    text = small_font.render(rightHand[0], True, 'white')
    screen.blit(text, ((rightOct * 245) - 165, HEIGHT - 55))
    text = small_font.render(rightHand[2], True, 'white')
    screen.blit(text, ((rightOct * 245) - 130, HEIGHT - 55))
    text = small_font.render(rightHand[4], True, 'white')
    screen.blit(text, ((rightOct * 245) - 95, HEIGHT - 55))
    text = small_font.render(rightHand[5], True, 'white')
    screen.blit(text, ((rightOct * 245) - 60, HEIGHT - 55))
    text = small_font.render(rightHand[7], True, 'white')
    screen.blit(text, ((rightOct * 245) - 25, HEIGHT - 55))
    text = small_font.render(rightHand[9], True, 'white')
    screen.blit(text, ((rightOct * 245) + 10, HEIGHT - 55))
    text = small_font.render(rightHand[11], True, 'white')
    screen.blit(text, ((rightOct * 245) + 45, HEIGHT - 55))
    text = small_font.render(rightHand[1], True, 'black')
    screen.blit(text, ((rightOct * 245) - 148, HEIGHT - 55))
    text = small_font.render(rightHand[3], True, 'black')
    screen.blit(text, ((rightOct * 245) - 113, HEIGHT - 55))
    text = small_font.render(rightHand[6], True, 'black')
    screen.blit(text, ((rightOct * 245) - 43, HEIGHT - 55))
    text = small_font.render(rightHand[8], True, 'black')
    screen.blit(text, ((rightOct * 245) - 8, HEIGHT - 55))
    text = small_font.render(rightHand[10], True, 'black')
    screen.blit(text, ((rightOct * 245) + 27, HEIGHT - 55))


def draw_title_bar(): #draws the different lines throughout
    instruction_text = medium_font.render('Up/Down Arrows Change Left Hand', True, 'black')
    screen.blit(instruction_text, (WIDTH - 510, 10))
    instruction_text2 = medium_font.render('Left/Right Arrows Change Right Hand', True, 'black')
    screen.blit(instruction_text2, (WIDTH - 510, 50))
    img = pygame.transform.scale(pygame.image.load('assets/logo.png'), [150, 150])
    screen.blit(img, (-20, -30))
    title_text = font.render('Python Programmable Piano!', True, 'white')
    screen.blit(title_text, (238, 18))
    title_text = font.render('Python Programmable Piano!', True, 'black')
    screen.blit(title_text, (240, 20))
    scale_text = nati_font.render('Q plus any key plays the minor scale of that key!', True, 'white') #MA
    screen.blit(scale_text, (910, 10))
    chord_text = nati2_font.render('W plus any key plays the seven chords of the minor key', True, 'white') #MA
    screen.blit(chord_text, (910, 50))
    chord_text = nati2_font.render('E plus any key plays the a 2-five-1 progression in the major key', True, 'white') #MA
    screen.blit(chord_text, (910, 80))


# NOTE
# NATI'S FUNCTIONS START HERE, functions defined below here are mine


def sample_text(): #A sample text I added that is activated by pressing a certain key later one
                   #Shows that altering layout is possible
    hi_text = medium_font.render('HELLO', True, 'black')
    screen.blit(hi_text, (WIDTH - 500, 30))
    

 #Empty dictionary to be filled with all the notes played of a certain scale

def minor_scale_mover(nowt): #plays a minor scale
    NOTE_KEY = {}
    index = piano_labels.index(nowt)
    nowt = piano_labels[index-2]
    index -= 2
    scale_track = 0
    scaler = 0 #crucial variable to keep determine if the next key should be a whole step away or a half step away
               #this is how I set up the pattern to play a minor scale
    SCALE_DEGREE = 1
    #global active_blacks, active_whites
    for increment in range(8):
        if scaler < 2:
            nowt = piano_labels[index+2]
        else:
            nowt = piano_labels[index+1]

        # four different conditions set up in order to be able to utilize the creator's method of coloring playing otesn
        # (I guess played notes in this case)
        if nowt[1] != '#' and scaler < 2: 
            index = piano_labels.index(nowt)
            scale_track += 1
            scaler += 1
            NOTE_KEY[nowt] = SCALE_DEGREE
            SCALE_DEGREE += 1
            piano_sounds[index].play() #returns next key
            second_index =white_notes.index(nowt) 
            active_whites.append([second_index, 120])
            #green_draw (active_whites, active_blacks)
            #print(active_whites, active_blacks)
        elif nowt[1] != '#' and scaler == 2: 
            index = piano_labels.index(nowt)
            scale_track += 1
            scaler = 0
            NOTE_KEY[nowt] = SCALE_DEGREE
            SCALE_DEGREE += 1
            piano_sounds[index].play()
            second_index = white_notes.index(nowt)
            active_whites.append([second_index, 120])
            #green_draw (active_whites, active_blacks)
            #print(active_whites, active_blacks)
        elif nowt[1] == '#' and scaler < 2: #and 'D' not in nowt and 'A' not in nowt:
            index = piano_labels.index(nowt)
            scale_track += 1
            scaler += 1
            NOTE_KEY[nowt] = SCALE_DEGREE
            SCALE_DEGREE += 1
            piano_sounds[index].play()
            second_index = black_labels.index(nowt)
            active_blacks.append([second_index, 120])
            #green_draw (active_whites, active_blacks)
            #print(active_whites, active_blacks)
        elif nowt[1] == '#' and scaler == 2: #and 'D' not in nowt and 'A' not in nowt:
            index = piano_labels.index(nowt)
            scale_track += 1
            scaler = 0
            NOTE_KEY[nowt] = SCALE_DEGREE
            SCALE_DEGREE += 1
            piano_sounds[index].play()
            second_index = black_labels.index(nowt)
            active_blacks.append([second_index, 120])
            #green_draw (active_whites, active_blacks)
            #print(active_whites, active_blacks)
        time.sleep(delay)

def chord_player (nowt):

    #defining pre-forloop conditions
    KEY_COLOR = (245, 0 , 0)
    NOTE_KEY = {} #empty dictionary for keeping information in the form of "note played: scale degree"
    index = piano_labels.index(nowt)
    nowt = piano_labels[index-2]
    index -= 2
    chord_track = 1 # a counter of sorts that keeps track of what note of the scale is being played
    is_major = False
    is_minor = True
    is_diminished = False
    scaler = 0
    SCALE_DEGREE = 1 # basically the same with chord_track but this is used for dictionary purposes
    third = 3
    fifth = 7
    #global active_blacks, active_whites

    # PRINTS RED FOR A QUICK SECOND AFTER CHORDS PLAY

    # I SHOULD DEFINE A FUNCTION THAT SPECIFICLALLY DOES THIS
    '''white_rects = []
    for i in range(52):
        rect = pygame.draw.rect(screen, KEY_COLOR, [i * 35, HEIGHT - 300, 35, 300], 0, 2) #The rectangles that represent the keys
        white_rects.append(rect)
        print ("Color is", KEY_COLOR)
        pygame.draw.rect(screen, 'black', [i * 35, HEIGHT - 300, 35, 300], 2, 2) #The outlines for these rectangles
        key_label = small_font.render(white_notes[i], True, 'black') #Configuring the font
        screen.blit(key_label, (i * 35 + 3, HEIGHT - 20))'''

    #start the for loop
    for increment in range(7):

        if scaler < 2:
            nowt = piano_labels[index+2]
        else:
            nowt = piano_labels[index+1]

        # determining the specific scale degrees at which specific types of chords are played
        # this part could be shorter but it is much clearer this why I think for someone that does not know scale degrees
        if chord_track == 8 or chord_track == 4 or chord_track == 5:
            is_minor = True
            is_major = False
            is_diminished = False
        elif chord_track == 3 or chord_track == 6 or chord_track == 7:
            is_minor = False
            is_major = True
            is_diminished = False
        elif chord_track == 2:
            is_minor = False
            is_major = False
            is_diminished = True

        if is_minor == True:
            third = 3
            fifth = 7
        elif is_major == True:
            third = 4
            fifth = 7
        elif is_diminished == True:
            third = 3
            fifth = 6

        # getting to the playing part...
        if nowt[1] != '#' and scaler < 2: 
            index = piano_labels.index(nowt)
            scaler += 1
            chord_track += 1
            NOTE_KEY[nowt] = SCALE_DEGREE
            SCALE_DEGREE += 1
            piano_sounds[index].play() # a triad is played everytime with these three play functions
            piano_sounds[index+third].play()
            piano_sounds[index+fifth].play() 
            second_index =white_notes.index(nowt) 
            active_whites.append([second_index, 120])
        elif nowt[1] != '#' and scaler == 2: 
            index = piano_labels.index(nowt)
            scaler = 0
            chord_track += 1
            NOTE_KEY[nowt] = SCALE_DEGREE
            SCALE_DEGREE += 1
            piano_sounds[index].play()
            piano_sounds[index+third].play()
            piano_sounds[index+fifth].play()
            second_index = white_notes.index(nowt)
            active_whites.append([second_index, 120])
            #green_draw (active_whites, active_blacks)
            #print(active_whites, active_blacks)
        elif nowt[1] == '#' and scaler < 2: #and 'D' not in nowt and 'A' not in nowt:
            index = piano_labels.index(nowt)
            chord_track += 1
            scaler += 1
            NOTE_KEY[nowt] = SCALE_DEGREE
            SCALE_DEGREE += 1
            piano_sounds[index].play()
            piano_sounds[index+third].play()
            piano_sounds[index+fifth].play()
            second_index = black_labels.index(nowt)
            active_blacks.append([second_index, 120])
            #green_draw (active_whites, active_blacks)
            #print(active_whites, active_blacks)
        elif nowt[1] == '#' and scaler == 2: #and 'D' not in nowt and 'A' not in nowt:
            index = piano_labels.index(nowt)
            chord_track += 1
            scaler = 0
            NOTE_KEY[nowt] = SCALE_DEGREE
            SCALE_DEGREE += 1
            piano_sounds[index].play()
            piano_sounds[index+third].play()
            piano_sounds[index+fifth].play()
            second_index = black_labels.index(nowt)
            active_blacks.append([second_index, 120])
            #green_draw (active_whites, active_blacks)
            #print(active_whites, active_blacks)
        #print(chord_track)
        #print(NOTE_KEY)
        time.sleep(delay)

def two_five_one(nowt): #WORKS!!
    
    chord_track = 1
    is_major = False 
    is_minor = True
    is_diminished = False
    scaler = 0
    index = piano_labels.index(nowt)
    play_index = index + 2
    for increment in range(3):
        if scaler == 1:
            is_major = True
            is_minor = False
            play_index = index + 7
        elif scaler == 2:
            play_index = index

        if is_minor == True:
            third = 3
            fifth = 7
        elif is_major == True:
            third = 4
            fifth = 7
        elif is_diminished == True:
            third = 3
            fifth = 6
        scaler += 1
        piano_sounds[play_index].play()
        piano_sounds[play_index+third].play()
        piano_sounds[play_index+fifth].play()
        time.sleep(1)
        

    

#CHEKCING ACCURACY OF INDICES WITH THESE TWO PRINT STATEMENTS. ACCURATE INDICES CHECKED.
#print(piano_sounds.index('C4.wav'))
#piano_sounds[39].play()


run = True
while run:
    left_dict = {'Z': f'C{left_oct}',
                 'S': f'C#{left_oct}',
                 'X': f'D{left_oct}',
                 'D': f'D#{left_oct}',
                 'C': f'E{left_oct}',
                 'V': f'F{left_oct}',
                 'G': f'F#{left_oct}',
                 'B': f'G{left_oct}',
                 'H': f'G#{left_oct}',
                 'N': f'A{left_oct}',
                 'J': f'A#{left_oct}',
                 'M': f'B{left_oct}'}

    right_dict = {'R': f'C{right_oct}',
                  '5': f'C#{right_oct}',
                  'T': f'D{right_oct}',
                  '6': f'D#{right_oct}',
                  'Y': f'E{right_oct}',
                  'U': f'F{right_oct}',
                  '8': f'F#{right_oct}',
                  'I': f'G{right_oct}',
                  '9': f'G#{right_oct}',
                  'O': f'A{right_oct}',
                  '0': f'A#{right_oct}',
                  'P': f'B{right_oct}'}

    timer.tick(fps)
    screen.fill('grey')
    print(len(active_whites))
    white_keys, black_keys, active_whites, active_blacks = draw_piano(active_whites, active_blacks)
    #white_keys, black_keys  = draw_piano(active_whites, active_blacks) #MY ATTEMPT TO CALL THIS GREEN SPECIFIC FUNCTION
    #active_whites, active_blacks = green_draw(active_whites,active_blacks) #MY ATTEMPT TO CALL THIS GREEN SPECIFIC FUNCTION
    draw_hands(right_oct, left_oct, right_hand, left_hand)
    draw_title_bar()





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            black_key = False
            for i in range(len(black_keys)):
                if black_keys[i].collidepoint(event.pos):
                    black_sounds[i].play(0, 3000)
                    black_key = True
                    active_blacks.append([i, 30])
                    print(active_blacks)
            for i in range(len(white_keys)):
                if white_keys[i].collidepoint(event.pos) and not black_key:
                    white_sounds[i].play(0, 3000)
                    active_whites.append([i, 30])
                    print(active_whites)


        if event.type == pygame.TEXTINPUT and not pygame.key.get_pressed()[pygame.K_q] and not pygame.key.get_pressed()[pygame.K_w] and not pygame.key.get_pressed()[pygame.K_e] : #THIS IS FOR SINGLE NOTE PLAYING
            if event.text.upper() in left_dict:
                if left_dict[event.text.upper()][1] == '#':
                    index = black_labels.index(left_dict[event.text.upper()])
                    black_sounds[index].play(0, 1000)
                    active_blacks.append([index, 30])
                else:
                    index = white_notes.index(left_dict[event.text.upper()])
                    white_sounds[index].play(0, 1000)
                    active_whites.append([index, 30])
            if event.text.upper() in right_dict:
                if right_dict[event.text.upper()][1] == '#':
                    index = black_labels.index(right_dict[event.text.upper()])
                    black_sounds[index].play(0, 1000)
                    active_blacks.append([index, 30])
                else:
                    index = white_notes.index(right_dict[event.text.upper()])
                    white_sounds[index].play(0, 1000)
                    active_whites.append([index, 30])

        if event.type == pygame.TEXTINPUT and event.text.upper() == 'F':
            delay += 0.1

        if event.type == pygame.TEXTINPUT and event.text.upper() == 'K' and delay - 0.1 != 0:   
            delay -= 0.1        



        #SCALE MODE ACCOMPLISHED, scales play properly #MA
        if event.type == pygame.TEXTINPUT and pygame.key.get_pressed()[pygame.K_q]:
            if event.text.upper() in left_dict:
                noteL = left_dict[event.text.upper()]
                sample_text()
                minor_scale_mover(noteL)
                
                
            if event.text.upper() in right_dict:
                if event.text.upper() in right_dict:
                    noteR = right_dict[event.text.upper()]
                    sample_text()
                    minor_scale_mover(noteR)
                    
        #CHORD MODE ACCOMPLISHED, chords play properly as well #MA
        if event.type == pygame.TEXTINPUT and pygame.key.get_pressed()[pygame.K_w]:
            if event.text.upper() in left_dict:
                noteL = left_dict[event.text.upper()]
                sample_text()
                chord_player(noteL)
            
            if event.text.upper() in right_dict:
                if event.text.upper() in right_dict:
                    noteR = right_dict[event.text.upper()]
                    sample_text()
                    chord_player(noteR)

         #251 mode
        if event.type == pygame.TEXTINPUT and pygame.key.get_pressed()[pygame.K_e]:
            if event.text.upper() in left_dict:
                noteL = left_dict[event.text.upper()]
                sample_text()
                two_five_one(noteL)
            
            if event.text.upper() in right_dict:
                if event.text.upper() in right_dict:
                    noteR = right_dict[event.text.upper()]
                    sample_text()
                    two_five_one(noteR)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if right_oct < 8:
                    right_oct += 1
            if event.key == pygame.K_LEFT:
                if right_oct > 0:
                    right_oct -= 1
            if event.key == pygame.K_UP:
                if left_oct < 8:
                    left_oct += 1
            if event.key == pygame.K_DOWN:
                if left_oct > 0:
                    left_oct -= 1

    pygame.display.flip() #pushes all the visual elements onto the screen in the correct order
pygame.quit()



    
# FAILED FUNCTIONS THAT COULD BE USED FOR LATER
'''def green_draw (active_whites, active_blacks): #(my attempt at isolating the green drawing function)
    print("HELLO")
    skip_count = 0
    last_skip = 2
    skip_track = 2
    for i in range(36):
        for q in range(len(active_blacks)):
            if active_blacks[q][0] == i:
                if active_blacks[q][1] > 0:
                    pygame.draw.rect(screen, 'red', [23 + (i * 35) + (skip_count * 35), HEIGHT - 300, 24, 200], 2, 2)
                    active_blacks[q][1] -= 1
                
        if last_skip == 2 and skip_track == 3:
            last_skip = 3
            skip_track = 0
            skip_count += 1
        elif last_skip == 3 and skip_track == 2:
            last_skip = 2
            skip_track = 0
            skip_count += 1
    for i in range(len(active_whites)):
        if active_whites[i][1] > 0:
            j = active_whites[i][0]
            pygame.draw.rect(screen, 'red', [j * 35, HEIGHT - 100, 35, 100], 2, 2)
            active_whites[i][1] -= 1 #This makes the pink last for as long as the fps or less
            #print('Hi')'''
