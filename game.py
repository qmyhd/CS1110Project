# # Names: Qais Youssef & Millie Pandya
# # Computing Id's: QMY6CV & vup7bv
# # Description of the game: This is a two player game that has two characters, Snow White and Prince Charming, as the user controlled characters.
# # One player will control Snow White using up, down, left, and right keys to collect apples that appear randomly on screen.
# # The second player will control Prince Charming using the W,A,S,D keys to collect those apples. Each apple collected gives the player one point,
# # and there is a countdown timer that gives both players 100 seconds to collect as many apples as possible.
# # Players will compete against each other to collect the most apples before the timer gets to 0. At the end, the player with the most apples wins.
#
# # Three Basic Features:
# # 1) User Input: Players will be able to use the arrow keys to move Snow White and Prince Charming.
# # 2) Game Over: Once the timer reaches 0, the game will be over. This includes a screen pop-up that says "Game Over" and along with the player that won.
# # 3) Graphics/Images: We will be using a field/grass background, with red apples. We will also be using two sprite sheets for Prince Charming and Snow White.
# # These are local image files, and are included in the project submission.
#
# # 4 Additional Features:
# # 1) Timer: Player has to collect more apples than the other player before the timer reaches 0. The timer starts at 100 and counts down.
# #    The timer can be seen on the top right of the screen.
# # 2) Sprite Animation: Sprite sheet animation of Snow White and Prince Charming is used to animate their movement.
# # 3) Two Players Simultaneously: Two people will control two different characters, Snow White and Prince Charming, simultaneously
# #    and using different sets of keys. These characters interact within the game as well, as if they touch each other, they will both lose an apple.
# # 4) Collectibles: There are multiple randomly appearing apple collectibles for the players to collect. Collection adds to a counter for each player,
# #    which can be seen on the top left and bottom right of the screen. These apples vanish when the players collect them, and reappear in other places.
# #    The players win by collecting the most apples.


import uvage, random

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
game_on = False


def setup():
    """
    this function sets up multiple global variables, and is meant to be run prior to the tick function to set up the game.
    it includes the images of the characters(sprites), apples, and background. it also sets up crucial values like the frames and
    timer. it also initializes the scores and score displays of both character's apple count.
    :return: initialized values for frames, timer, apple scores, as well as necessary gameboxes like sprite, score display
    """
    global camera, frame, snow_white_on,snow_white_move, snow_white_on, snow_white, \
        snow_white_up, snow_white_down, snow_white_right, snow_white_left, score_apples_SW, score_box_SW, grass_background,\
        apples, SW_life, prince_charming_on, prince_charming_down, prince_charming_up,\
        prince_charming_left, prince_charming_right, prince_charming_move, frame_p, prince_charming, score_box_PC,\
        score_apples_PC, PC_life, timer, game_on, game_end
    camera = uvage.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
    frame = 0  # will control how quickly sprite (Snow White) goes through sprite sheet, displays her still image
    frame_p = 0 # will control how quickly sprite (Prince C.) goes through sprite sheet, displays his still image
    snow_white_on = True  # Snow White is alive
    prince_charming_on = True # Prince Charming is alive
    game_on = False
    game_end = False
    timer = 100
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
    prince_charming = uvage.from_image(200, 200, prince_charming_down[0])
    prince_charming.scale_by(2)
    # all above prince charming images are from https://www.deviantart.com/slimmmeiske2/art/RMXP-Sprite-Disney-s-Prince-Charming-352610928
    prince_charming_move = False

    score_apples_SW = 0
    score_apples_PC = 0
    score_box_SW = uvage.from_text(650, 550, "Snow's Apples: " + str(score_apples_SW), 40, 'white', bold=True)
    score_box_PC = uvage.from_text(150, 30, "Prince's Apples: " + str(score_apples_PC), 40, 'red')

    # random locations from x=55 to 85% of the screen width
    rand_location_x1 = random.randint(55, 750)
    rand_location_x2 = random.randint(55, 750)
    rand_location_x3 = random.randint(55, 750)
    # random locations from y=55 to 85% of the screen height
    rand_location_y1 = random.randint(48, 550)
    rand_location_y2 = random.randint(48, 550)
    rand_location_y3 = random.randint(48, 550)
    apples = [
        uvage.from_image(rand_location_x1, rand_location_y1, "apple_good.png"),
        uvage.from_image(rand_location_x2, rand_location_y2, "apple_good.png"),
        uvage.from_image(rand_location_x3, rand_location_y3, "apple_good.png")
    ]
    for each in apples:
        each.scale_by(2)
    # apple: https://www.deviantart.com/xxdowntoearthfooxx/art/Gala-Apple-834004646

def start_screen():
    """
    this function displays the text on the start screen if the game has not started yet
    :return: input for game to begin
    """
    global game_on
    if game_on == False and game_end == False:
        camera.clear('light green')
        camera.draw(uvage.from_text(400, 100, "Apple Picking <3", 70, "red"))
        camera.draw(uvage.from_text(400, 200, "Your First Date", 60, "white"))
        camera.draw(uvage.from_text(400, 250, "Snow White and Prince Charming are on their first date,", 25, "white"))
        camera.draw(uvage.from_text(400, 270, "and decide to have an apple picking competition", 25, "white"))
        camera.draw(uvage.from_text(400, 300, "Snow White moves using the arrow keys, Prince Charming moves using WASD keys", 25, "white"))
        camera.draw(uvage.from_text(400, 350, "Both players will try to collect as many apples as possible before the timer runs out", 25, "white"))
        camera.draw(uvage.from_text(400, 378, "Be careful (or not careful) to hit each other, as you will both lose an apple", 25, "white"))
        camera.draw(uvage.from_text(400, 420, "Whoever has the most apples at the end wins their date!!", 35, "white"))
        camera.draw(uvage.from_text(400, 500, "Press the space bar to begin your date <3", 55, "red"))
        if uvage.is_pressing("space"):
            game_on = True

def player_interaction():
    """
    this function controls player interaction, and takes away an apple from each player if they touch
    :return: updated score box for both players 
    """
    global snow_white, prince_charming, score_apples_SW, score_apples_PC, score_box_SW, score_box_PC
    if snow_white.touches(prince_charming):
        score_apples_PC -= .03
        score_apples_SW -= .03
    camera.draw(score_box_PC, score_box_SW)


def draw_environment():
    """
    this function draws the grass background after the tick function is called
    :return: N/A
    """
    global grass_background
    camera.draw(grass_background)


def handle_SW_apples():
    """
    this function handles Snow White's apples, as it makes them disappear and reappear after Snow White collects them, and 
    updates her score on the screen 
    :return: new score for Snow White 
    """
    global camera, apples, score_apples_SW, score_box_SW
    # new location for apple if touched
    for apple in apples:
        if snow_white.touches(apple):
            score_apples_SW += 1
            new_random_x = random.randint(55, 750)
            new_random_y = random.randint(48, 550)
            apple.x = new_random_x
            apple.y = new_random_y
        camera.draw(apple)
    # updates score on screen for collected apple
    if int(score_apples_SW) < 0:
        score_apples_SW = 0
    score_box_SW = uvage.from_text(650, 550, "Snow's Apples: " + str(int(score_apples_SW)), 40, 'white', bold=True)
    camera.draw(score_box_SW)

def handle_PC_apples():
    """
    this function handles Prince Charming's apples, as it makes them disappear and reappear after Prince Charming collects them, and 
    updates his score on the screen 
    :return: new score for Prince Charming
    """
    global camera, apples, score_apples_PC, score_box_PC
    # new location for apple if touched
    for apple in apples:
        if prince_charming.touches(apple):
            score_apples_PC += 1
            new_random_x = random.randint(55, 750)
            new_random_y = random.randint(48, 550)
            apple.x = new_random_x
            apple.y = new_random_y
        camera.draw(apple)
    # updates score on screen for collected apple
    if int(score_apples_PC) < 0:
        score_apples_PC = 0
    score_box_PC = uvage.from_text(150, 30, "Prince's Apples: " + str(int(score_apples_PC)), 40, 'red')
    camera.draw(score_box_PC)


def move_snow_white():
    """
    this function controls the movements of Snow White, the animated sprite, via keyboard input of arrow keys 
    :return: updated image of Snow White 
    """
    global snow_white_move, snow_white_on, snow_white, frame, snow_white_up,\
        snow_white_down, snow_white_right, snow_white_left
    snow_white_move = False
    if snow_white_on:
        speed = 7
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
    """
        this function controls the movements of Prince Charming, the animated sprite, via keyboard input of WASD 
        :return: updated image of Prince Charming
    """
    global prince_charming_move, prince_charming_on, prince_charming, frame_p, prince_charming_up,\
        prince_charming_down, prince_charming_right, prince_charming_left
    prince_charming_move = False
    if prince_charming_on:
        speed = 7
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

def endgame():
    """
    this function displays the game over screen once the game has ended according to the timer in tick 
    :return: game over screen with the winner 
    """
    global game_end
    if game_end == True:
        camera.clear('light green')
        if score_apples_SW > score_apples_PC:
            camera.draw(uvage.from_text(camera.x, camera.y, "Game Over! Snow White Wins!!", 50, 'black'))
        if score_apples_PC > score_apples_SW:
            camera.draw(uvage.from_text(camera.x, camera.y, "Game Over! Prince Charming Wins!!", 50, 'black'))
        if score_apples_SW == score_apples_PC:
            camera.draw(uvage.from_text(camera.x, camera.y, "Game Over! The couple TIES!!", 50, 'black'))

def tick():
    """
    if the game isn't on, this function displays the start screen
    once the game has begun, this function loads all the other functions to play the game and controls the timer, which
    counts down the time the players have left to collect their apples 
    once the timer is at 0, this function will end the game 
    :return: updates the game_on and game_end variables 
    """
    global timer, game_on, score_apples_PC, score_apples_SW, game_end
    if game_on == False:
        start_screen()
    if game_on == True:
        draw_environment()
        handle_PC_apples()
        handle_SW_apples()
        move_prince_charming()
        move_snow_white()
        player_interaction()
        timer -= .03
        camera.draw("Time Left: " + str(int(timer)), 36, "white", 700, 50)
    if timer <= 0:
        game_end = True
        endgame()
    camera.display()

setup()
uvage.timer_loop(30, tick)
