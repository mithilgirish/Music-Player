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
UIimage = pygame.transform.scale(pygame.image.load(image_path), (800, 600))

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

play_path = 'UI_images/play.png'
pause_path = 'UI_images/pause.png'
back_path = 'UI_images/back.png'
next_path = 'UI_images/next.png'

volume_path = 'UI_images/volumeUI.png'
volumeBar_path = 'UI_images/volumeBar.png'
volumeC_path = 'UI_images/volumeC.png'

albumH_path = 'UI_images/AlbumHolder.png'

album_path = 'album_photo'

ALBUMSIZE = 200

ALBUMSIZEH = 42

UISIZE = 50

PlayIMG = pygame.transform.scale(pygame.image.load(play_path), (UISIZE, UISIZE))
PauseIMG = pygame.transform.scale(pygame.image.load(pause_path), (UISIZE + 2, UISIZE + 2))
BackIMG = pygame.transform.scale(pygame.image.load(back_path), (UISIZE, UISIZE))
NextIMG = pygame.transform.scale(pygame.image.load(next_path), (UISIZE, UISIZE))

VolumeIMG = pygame.transform.scale(pygame.image.load(volume_path), (220, 45))
VolumeCIMG = pygame.transform.scale(pygame.image.load(volumeC_path), (30, 30))

albumIMGs = [os.path.join(album_path, f) for f in os.listdir(album_path) if f.endswith((".png", ".jpg"))]


albumHolderIMG = pygame.transform.scale(pygame.image.load(albumH_path), (ALBUMSIZE+ALBUMSIZEH+2, ALBUMSIZE+ALBUMSIZEH+2))

album_list = [os.path.splitext(file)[0] for file in os.listdir(album_path) if os.path.isfile(os.path.join(album_path, file))]


# Define fonts
Font_path = "Font/ITCAvantGarde.ttf"
font_large = pygame.font.Font(Font_path, 34)
font_Playing = pygame.font.Font(Font_path, 28)
font_small = pygame.font.Font(Font_path, 21)

# Define layout dimensions
CONTROLS_HEIGHT = 100
SONG_LIST_WIDTH = 300
VOLUME_SLIDER_HEIGHT = 20
TIME_DISPLAY_HEIGHT = 30

# Define layout positions
HEADER_X = 30
HEADER_Y = 330
CONTROLS_X = 32
CONTROLS_Y = 440
SONG_LIST_X = 310
SONG_LIST_Y = 115
VOLUME_SLIDER_X = 65
VOLUME_SLIDER_Y = 520
TIME_DISPLAY_X = 32
TIME_DISPLAY_Y = 395 

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
        songD_list = song_info.split(',,,')
        SongName = songD_list[0]
        AlbumName = songD_list[1]
        ArtistName = songD_list[2]
        file_index = album_list.index(AlbumName)
        albumIMG = pygame.transform.scale(pygame.image.load(albumIMGs[file_index]), (ALBUMSIZE, ALBUMSIZE))
        artist_text = font_small.render(ArtistName, True, GRAY)
        song_text = font_Playing.render(SongName, True, WHITE)
        window.blit(albumIMG, (29, 107))
        window.blit(song_text, (HEADER_X, HEADER_Y))
        window.blit(artist_text, (HEADER_X, HEADER_Y + 30))

# Function to draw the playback controls
def draw_controls():
    play_icon = PlayIMG if not pygame.mixer.music.get_busy() else PauseIMG
    prev_x = CONTROLS_X
    play_x = prev_x + 70
    next_x = play_x + 70
    window.blit(BackIMG, (prev_x, CONTROLS_Y))
    window.blit(NextIMG, (next_x, CONTROLS_Y))
    window.blit(play_icon, (play_x, CONTROLS_Y))

# Function to draw the song list
def draw_song_list():
    for i, song_path in enumerate(music_files):

        song_info = os.path.splitext(os.path.basename(song_path))[0]
        songD_list = song_info.split(',,,')
        SongName = songD_list[0]
        AlbumName = songD_list[1]
        ArtistName = songD_list[2]
        
        title_text = font_small.render(SongName, True, WHITE)
        album_text = font_small.render(AlbumName, True, WHITE)
        artist_text = font_small.render(ArtistName, True, GRAY)  
        title_x = SONG_LIST_X
        title_y = SONG_LIST_Y + 10 + i * 70
        artist_y = title_y + title_text.get_height() + 5
        Num = font_small.render(str(i + 1), True, WHITE)
        window.blit(Num, (title_x - 35, title_y))
        window.blit(title_text, (title_x, title_y))
        window.blit(album_text, (title_x+263, title_y))
        window.blit(artist_text, (title_x, artist_y))

# Function to format time in MM:SS
def format_time(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02}:{seconds:02}"

# Function to draw the current playback time
def draw_playback_time(current_time, total_time):
    time_text = f"{format_time(current_time)} / {format_time(total_time)}"
    time_surface = font_small.render(time_text, True, WHITE)
    window.blit(time_surface, (TIME_DISPLAY_X, TIME_DISPLAY_Y))

# Function to draw the volume slider
def draw_volume_slider():
    slider_width = 163

    window.blit(VolumeIMG,(15,510))


    
    

    volume_rect_width = int(volume * slider_width)
    VolumeBarIMG = pygame.transform.scale(pygame.image.load(volumeBar_path), (volume_rect_width, 10))
    window.blit(VolumeBarIMG,(VOLUME_SLIDER_X-5,529))
    window.blit(VolumeCIMG,(VOLUME_SLIDER_X+volume_rect_width -15,520))
    

    

    #pygame.draw.rect(window, WHITE, volume_rect)



def FindSongLenght(current_song):
    return pygame.mixer.Sound(current_song).get_length()


current_song = music_files[0]
TotalLenght = FindSongLenght(current_song)
# Game loop

current_time = 0
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if CONTROLS_X <= mouse_pos[0] <= CONTROLS_X + 50 and CONTROLS_Y <= mouse_pos[1] <= CONTROLS_Y + UISIZE:
                # Previous button
                current_index = (current_index - 1) % len(music_files)
                current_song = music_files[current_index]
                TotalLenght =  FindSongLenght(current_song)
                pygame.mixer.music.load(current_song)
                pygame.mixer.music.play()
            elif CONTROLS_X + 70 <= mouse_pos[0] <= CONTROLS_X + 120 and CONTROLS_Y <= mouse_pos[1] <= CONTROLS_Y + UISIZE:
                # Play/Pause button
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif CONTROLS_X + 140 <= mouse_pos[0] <= CONTROLS_X + 190 and CONTROLS_Y <= mouse_pos[1] <= CONTROLS_Y + UISIZE:
                # Next button
                current_index = (current_index + 1) % len(music_files)
                current_song = music_files[current_index]
                TotalLenght =  FindSongLenght(current_song)
                pygame.mixer.music.load(current_song)
                pygame.mixer.music.play()
            elif VOLUME_SLIDER_X <= mouse_pos[0] <= VOLUME_SLIDER_X + 163 and VOLUME_SLIDER_Y <= mouse_pos[1] <= VOLUME_SLIDER_Y + VOLUME_SLIDER_HEIGHT:
                # Volume slider
                volume = (mouse_pos[0] - VOLUME_SLIDER_X) /163
                pygame.mixer.music.set_volume(volume)

    # Draw the playback time
    if pygame.mixer.music.get_busy():
        current_time = pygame.mixer.music.get_pos() / 1000  # Convert from milliseconds to seconds

    if current_time > TotalLenght:
        current_index = (current_index + 1) % len(music_files)
        current_song = music_files[current_index]
        TotalLenght =  FindSongLenght(current_song)
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play()

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

    draw_playback_time(current_time, TotalLenght)

    window.blit(albumHolderIMG, (28-(ALBUMSIZEH//2), 106-(ALBUMSIZEH//2)))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
