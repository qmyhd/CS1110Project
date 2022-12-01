# Names: Qais Youssef & Millie Pandya
# Computing Id's: QMY6CV & vup7bv
# Description of the game: This game will use a character (Snow White) as the main
# object that players will control. Using up, down, left, and right keys, players will control Snow White's
# movement to collect apples that appear randomly on screen. Players have 5 minutes to collect 5 apples to win.
# Each apple collected gives the player one point, and it takes 5 points to win the game. Unfortunately
# there are also poison apples falling from the top, and Snow White must avoid them while collecting apples.
# Any time Snow White accidentally touches a poison apple, her health bar decreases in size. Once the health bar is
# exhausted, the player loses the game.

# Three Basic Features:
# 1) User Input: Players will be able to use the arrow keys to move Snow White.
# 2) Game Over: If Snow White collects too many poison apples, her health bar will be exhausted and the game will end.
# 3) Graphics/Images: We will be using a field/grass background, with "good" red apples, and poison apples.
#   There will also be a witch that pops out for the game over screen.

# 4 Additional Features:
# 1) Timer: Player has to collect 5 apples within 5 minutes without depleting their health bar to win the game.
# 2) Sprite Animation: Sprite sheet animation of Snow White will be used to animate her walking motions.
# 3) Enemies: The poison apples will fall from the top of the screen, and Snow White will have to avoid them to avoid
#   decreasing her health bar. Once the health bar is exhausted, the player loses the game.
# 4) Collectibles: Apples will be collected, with a counter of num. collected, and a goal of 5 to reach to win the game.
# 5) Health Bar: There will be a health bar that decreases each time Snow White hits a poison apple.
#   Once the health bar is exhausted, the player loses the game.

import uvage, random

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

def setup():
    global camera, frame, snow_white_on,snow_white_move, snow_white_on, snow_white, frame, \
        snow_white_up, snow_white_down, snow_white_right, snow_white_left, score_apples_SW, score_box_SW, grass_background,\
        apples, poison_apples, life, health_bar, prince_charming_on, prince_charming_down, prince_charming_up,\
        prince_charming_left, prince_charming_right, prince_charming_move, frame_p, prince_charming, score_box_PC,\
        score_apples_PC
    camera = uvage.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
    frame = 0  # will control how quickly sprite (Snow White) goes through sprite sheet, displays her still image
    frame_p = 0 # will control how quickly sprite (Prince C.) goes through sprite sheet, displays his still image
    snow_white_on = True  # Snow White is alive
    prince_charming_on = True # Prince Charming is alive
    grass_background = uvage.from_image(0, 600, "grass_background.png")
    grass_background.scale_by(2.2)
    # background: https://www.deviantart.com/axze/art/Blade-of-Magic-Tiles-2-481826099

    snow_white_down = uvage.load_sprite_sheet("snow_white_sprite_sheet_down.png", rows=1, columns=4)
    snow_white_up = uvage.load_sprite_sheet("snow_white_sprite_sheet_up.png", rows=1, columns=4)
    snow_white_left = uvage.load_sprite_sheet("snow_white_sprite_sheet_left.png", rows=1, columns=4)
    snow_white_right = uvage.load_sprite_sheet("snow_white_sprite_sheet_right.png", rows=1, columns=4)
    snow_white = uvage.from_image(100, 200, snow_white_down[0])
    snow_white.scale_by(2)
    # all above snow_white images are from https://www.deviantart.com/slimmmeiske2/art/RMXP-Sprite-Disney-s-Snow-White-274961875
    snow_white_move = False

    prince_charming_down = uvage.load_sprite_sheet("prince_charming_sprite_sheet_down.png", rows=1, columns=4)
    prince_charming_up = uvage.load_sprite_sheet("prince_charming_sprite_sheet_up.png", rows=1, columns=4)
    prince_charming_left = uvage.load_sprite_sheet("prince_charming_sprite_sheet_left.png", rows=1, columns=4)
    prince_charming_right = uvage.load_sprite_sheet("prince_charming_sprite_sheet_right.png", rows=1, columns=4)
    prince_charming = uvage.from_image(100, 200, prince_charming_down[0])
    prince_charming.scale_by(2)
    # all above prince charming images are from https://www.deviantart.com/slimmmeiske2/art/RMXP-Sprite-Disney-s-Prince-Charming-352610928
    prince_charming_move = False

    score_apples_SW = 0
    score_apples_PC = 0
    score_box_SW = uvage.from_text(150, 30, "Snow's Apples: " + str(score_apples_SW), 40, 'red')
    score_box_PC = uvage.from_text(400, 400, "Prince's Apples: " + str(score_apples_PC), 40, 'red')

    # random locations from x=55 to 85% of the screen width
    rand_location_x1 = random.randint(55, 750)
    rand_location_x2 = random.randint(55, 750)
    rand_location_x3 = random.randint(55, 750)
    # random locations from y=55 to 85% of the screen height
    rand_location_y1 = random.randint(48, 550)
    rand_location_y2 = random.randint(48, 550)
    rand_location_y3 = random.randint(48, 550)
    apples = [
        uvage.from_image(rand_location_x1, rand_location_y1, "good_apple.png"),
        uvage.from_image(rand_location_x2, rand_location_y2, "good_apple.png"),
        uvage.from_image(rand_location_x3, rand_location_y3, "good_apple.png")
    ]
    for each in apples:
        each.scale_by(.1)
    # apple: https://freesvg.org/red-apple-remix
    rand_location_x4 = random.randint(55, int(.85 * SCREEN_WIDTH))
    rand_location_x5 = random.randint(55, int(.85 * SCREEN_WIDTH))
    poison_apples = [
        uvage.from_image(rand_location_x1, 10, "poison_apple.png"),
        uvage.from_image(rand_location_x2, 10, "poison_apple.png"),
        uvage.from_image(rand_location_x3, 10, "poison_apple.png"),
        uvage.from_image(rand_location_x4, 10, "poison_apple.png"),
        uvage.from_image(rand_location_x5, 10, "poison_apple.png"),
    ]
    life = 100
    health_bar = uvage.from_color(450, 100, "red", life, 35)


def draw_environment():
    global grass_background
    camera.draw(grass_background)


def handle_apples():
    global camera, apples, score_apples_SW, score_apples_PC, score_box_SW, score_box_PC
    # new location for apple if touched
    for apple in apples:
        if snow_white.touches(apple):
            score_apples_SW += 1
            new_random_x = random.randint(55, 750)
            new_random_y = random.randint(48, 550)
            apple.x = new_random_x
            apple.y = new_random_y
        if prince_charming.touches(apple):
            score_apples_PC += 1
            new_random_x = random.randint(55, 750)
            new_random_y = random.randint(48, 550)
            apple.x = new_random_x
            apple.y = new_random_y
    camera.draw(apple)
    # updates score on screen for collected apple
    score_box_SW = uvage.from_text(150, 30, "Snow's Apples: " + str(score_apples_SW), 40, 'red')
    score_box_PC = uvage.from_text(400, 400, "Prince's Apples: " + str(score_apples_PC), 40, 'red')
    camera.draw(score_box_SW, score_box_PC)

def handle_poison_apples():
    global camera, poison_apples, snow_white, life, health_bar
    for p_apple in poison_apples:
        speed = random.randint(3, 8)
        p_apple.speedy = speed
    for p_apple in poison_apples:
        if p_apple.touches(snow_white):
            life -= 20
        # updates health bar if hit by poison apple
        health_bar = uvage.from_color(450, 100, "red", life, 35)
        camera.draw(health_bar)


def move_snow_white():
    global snow_white_move, snow_white_on, snow_white, frame, snow_white_up,\
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
        camera.draw(snow_white)


def move_prince_charming():
    global prince_charming_move, prince_charming_on, prince_charming, frame_p, prince_charming_up,\
        prince_charming_down, prince_charming_right, prince_charming_left
    prince_charming_move = False
    if prince_charming_on:
        speed = 5
        if uvage.is_pressing("w"):
            prince_charming.y -= speed
            prince_charming_move = True
            frame_p += .3
            if frame_p >= 4:
                frame_p = 0
            prince_charming.image = prince_charming_up[int(frame_p)]
        if uvage.is_pressing("s"):
            prince_charming.y += speed
            prince_charming_move = True
            frame_p += .3
            if frame_p >= 4:
                frame_p = 0
            prince_charming.image = prince_charming_down[int(frame_p)]
        if uvage.is_pressing("d"):
            prince_charming.x += speed
            prince_charming_move = True
            frame_p += .3
            if frame_p >= 4:
                frame_p = 0
            prince_charming.image = prince_charming_right[int(frame_p)]
        if uvage.is_pressing("a"):
            prince_charming.x -= speed
            prince_charming_move = True
            frame_p += .3
            if frame_p >= 4:
                frame_p = 0
            prince_charming.image = prince_charming_left[int(frame_p)]
        if prince_charming_move == False:
            prince_charming.image = prince_charming_down[0]
        camera.draw(prince_charming)

def tick():
    draw_environment()
    handle_apples()
    handle_poison_apples()
    move_prince_charming()
    move_snow_white()
    camera.display()

setup()
uvage.timer_loop(30, tick)
