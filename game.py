# Names: Qais Youssef & Millie Pandya
#Computing Id's: QMY6CV & vup7bv
#Description of the game: This game will use a character (Snow White) as the main
#object that players will control. Using (W,A,S,D), players will control Snow White's
#movement to collect apples that appear randomly on screen. Players have 5 minutes to collect 5 apples to win.
#Each apple collected gives the player one point, and it takes 5 points to win the game. Unfortunately
#there are also poison apples falling from the top, and Snow White must avoid them while collecting apples.
#Any time Snow White accidentally touches a poison apple, her health bar decreases in size. Once the health bar is exhausted, the player loses the game.

#Three Basic Features:
#1) User Input: Players will be able to use the arrow keys or (W,A,S,D) to move Snow White.
#2) Game Over: If Snow White collects too many poison apples, her health bar will be exhausted and the game will end.
#3) Graphics/Images: We will be using a field/grass background, with "good" red apples, and poison apples.
#   There will also be a witch that pops out for the game over screen.

#4 Additional Features:
#1) Timer: Player has to collect 5 apples within 5 minutes without depleting their health bar to win the game.
#2) Sprite Animation: Sprite sheet animation of Snow White will be used to animate her walking motions.
#3) Enemies: The poison apples will fall from the top of the screen, and Snow White will have to avoid them to avoid
#   decreasing her health bar. Once the health bar is exhausted, the player loses the game.
#4) Collectibles: Apples will be collected, with a counter of collected apples, and a goal of 5 to reach to win the game.
#5) Health Bar: There will be a healthbar that decreases each time Snow White hits a poison apple.
#   Once the health bar is exhausted, the player loses the game.

import uvage, random

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

def setup():
    global camera, frame, snow_white_on,snow_white_move, sw_facing_right, snow_white_on, snow_white, frame, \
        snow_white_up, snow_white_down, snow_white_right, snow_white_left, score_apples, score_box, grass_background
    camera = uvage.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
    frame = 0  # will control how quickly sprite (Snow White) goes through sprite sheet, displays her still image
    snow_white_on = True  # Snow White is alive
    sw_facing_right = True  ###check at the end if this is even necessary
    snow_white_down = uvage.load_sprite_sheet("snow_white_sprite_sheet_down.png", rows=1, columns=4)
    snow_white_up = uvage.load_sprite_sheet("snow_white_sprite_sheet_up.png", rows=1, columns=4)
    snow_white_left = uvage.load_sprite_sheet("snow_white_sprite_sheet_left.png", rows=1, columns=4)
    snow_white_right = uvage.load_sprite_sheet("snow_white_sprite_sheet_right.png", rows=1, columns=4)
    snow_white = uvage.from_image(100, 200, snow_white_down[0])
    snow_white_move = False
    score_apples = 0
    score_box = uvage.from_text(55, 55, 'Apples: ' + str(score_apples), 40, 'red')
    grass_background = uvage.from_image(0, 600, "grass_background.png")
    grass_background.scale_by(3)
    apples = [

    ]

def draw_environment():
    global grass_background
    camera.draw(grass_background)

def move_snow_white():
    global snow_white_move, sw_facing_right, snow_white_on, snow_white, frame, snow_white_up,\
        snow_white_down, snow_white_right, snow_white_left
    snow_white_move = False
    if snow_white_on:
        speed = 5
        if uvage.is_pressing("up arrow"):
            snow_white.y -= speed
            snow_white_move = True
            frame += .3
            if frame >= 4:
                frame = 0
            snow_white.image = snow_white_up[int(frame)]
        if uvage.is_pressing("down arrow"):
            snow_white.y += speed
            snow_white_move = True
            frame += .3
            if frame >= 4:
                frame = 0
            snow_white.image = snow_white_down[int(frame)]
        if uvage.is_pressing("right arrow"):
            snow_white.x += speed
            snow_white_move = True
            frame += .3
            if frame >= 4:
                frame = 0
            snow_white.image = snow_white_right[int(frame)]
        if uvage.is_pressing("left arrow"):
            snow_white.x -= speed
            snow_white_move = True
            frame += .3
            if frame >= 4:
                frame = 0
            snow_white.image = snow_white_left[int(frame)]
        if snow_white_move == False:
            snow_white.image = snow_white_down[0]




