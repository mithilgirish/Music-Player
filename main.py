import pygame
import os

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Music Player")

image_path = 'UI_images/MainUI.png'
UIimage = pygame.transform.scale(pygame.image.load(image_path), (800,600)) 
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

play_path = 'UI_images/play.png'
pause_path = 'UI_images/pause.png'
back_path = 'UI_images/back.png'
next_path = 'UI_images/next.png'

UISIZE = 50

PlayIMG = pygame.transform.scale(pygame.image.load(play_path), (UISIZE,UISIZE)) 
PauseIMG = pygame.transform.scale(pygame.image.load(pause_path), (UISIZE+2,UISIZE+2)) 
BackIMG = pygame.transform.scale(pygame.image.load(back_path), (UISIZE,UISIZE)) 
NextIMG = pygame.transform.scale(pygame.image.load(next_path), (UISIZE,UISIZE)) 


# Define fonts
Font_path = "Font/ITCAvantGarde.ttf"
font_large = pygame.font.Font(Font_path, 34)
font_Playing = pygame.font.Font(Font_path, 28)
font_small = pygame.font.Font(Font_path, 21)

# Define layout dimensions

CONTROLS_HEIGHT = 100
SONG_LIST_WIDTH = 300
VOLUME_SLIDER_HEIGHT = 20

# Define layout positions
HEADER_X = 30
HEADER_Y = 330

CONTROLS_X = 32
CONTROLS_Y = 400
SONG_LIST_X = 310
SONG_LIST_Y = 110
VOLUME_SLIDER_X = CONTROLS_X 
VOLUME_SLIDER_Y = CONTROLS_Y + CONTROLS_HEIGHT + 10

# Load music files
music_dir = "Songs"
music_files = [os.path.join(music_dir, f) for f in os.listdir(music_dir) if f.endswith((".mp3", ".wav"))]

# Initialize variables
current_index = 0
volume = 0.5
pygame.mixer.music.set_volume(volume)

# Load the first song
if music_files:
    current_song = music_files[current_index]
    pygame.mixer.music.load(current_song)
    pygame.mixer.music.play()

# Function to draw the header
def draw_header():
    

    if music_files:
        song_info = os.path.splitext(os.path.basename(current_song))[0]
        artist_text = font_small.render("Artist Name", True, GRAY) 
        song_text = font_Playing.render(song_info, True, WHITE)
        window.blit(song_text, (HEADER_X , HEADER_Y ))
        window.blit(artist_text, (HEADER_X, HEADER_Y + 30))

# Function to draw the playback controls
def draw_controls():

    play_icon = PlayIMG if not pygame.mixer.music.get_busy() else PauseIMG


    prev_x = CONTROLS_X 
    play_x = prev_x + 70
    next_x = play_x + 70
    window.blit(BackIMG, (prev_x, CONTROLS_Y ))
    window.blit(NextIMG, (next_x, CONTROLS_Y ))
    window.blit(play_icon, (play_x, CONTROLS_Y ))


    

# Function to draw the song list
def draw_song_list():
    for i, song_path in enumerate(music_files):
        song_info = os.path.splitext(os.path.basename(song_path))[0]
        title_text = font_small.render(song_info, True, WHITE)
        artist_text = font_small.render("Artist Name", True, GRAY)  # Replace with actual artist information

        title_x = SONG_LIST_X 
        title_y = SONG_LIST_Y + 10 + i * 70
        artist_y = title_y + title_text.get_height() + 5

        Num = font_small.render(str(i+1), True, WHITE)

        window.blit(Num, (title_x -35 , title_y))

        window.blit(title_text, (title_x, title_y))
        window.blit(artist_text, (title_x, artist_y))

# Function to draw the volume slider
def draw_volume_slider():
    slider_width = 200
    slider_height = VOLUME_SLIDER_HEIGHT
    slider_rect = pygame.Rect(VOLUME_SLIDER_X, VOLUME_SLIDER_Y, slider_width, slider_height)
    pygame.draw.rect(window, GRAY, slider_rect)

    volume_rect_width = int(volume * slider_width)
    volume_rect = pygame.Rect(VOLUME_SLIDER_X, VOLUME_SLIDER_Y, volume_rect_width, slider_height)
    pygame.draw.rect(window, WHITE, volume_rect)

# Game loop
running = True
while running:
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if CONTROLS_X + 10 <= mouse_pos[0] <= CONTROLS_X + 60 and \
               CONTROLS_Y <= mouse_pos[1] <= CONTROLS_Y + CONTROLS_HEIGHT:
                # Previous button
                current_index = (current_index - 1) % len(music_files)
                current_song = music_files[current_index]
                pygame.mixer.music.load(current_song)
                pygame.mixer.music.play()
            elif CONTROLS_X + 60 <= mouse_pos[0] <= CONTROLS_X + 110 and \
                 CONTROLS_Y <= mouse_pos[1] <= CONTROLS_Y + CONTROLS_HEIGHT:
                # Play/Pause button
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif CONTROLS_X + 110 <= mouse_pos[0] <= CONTROLS_X + 160 and \
                 CONTROLS_Y <= mouse_pos[1] <= CONTROLS_Y + CONTROLS_HEIGHT:
                # Next button
                current_index = (current_index + 1) % len(music_files)
                current_song = music_files[current_index]
                pygame.mixer.music.load(current_song)
                pygame.mixer.music.play()
            elif VOLUME_SLIDER_X <= mouse_pos[0] <= VOLUME_SLIDER_X + 200 and \
                 VOLUME_SLIDER_Y <= mouse_pos[1] <= VOLUME_SLIDER_Y + VOLUME_SLIDER_HEIGHT:
                # Volume slider
                volume = (mouse_pos[0] - VOLUME_SLIDER_X) / 200
                pygame.mixer.music.set_volume(volume)

    # Clear the window
    window.fill(BLACK)
    window.blit(UIimage, (0, 0)) 

    # Draw the header
    draw_header()

    # Draw the playback controls
    draw_controls()

    # Draw the song list
    draw_song_list()

    # Draw the volume slider
    draw_volume_slider()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()