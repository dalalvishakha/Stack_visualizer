
import pygame
import time

pygame.init()

# --------------------------------
# WINDOW
# --------------------------------

WIDTH = 900
HEIGHT = 650

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stack Visualiser")

clock = pygame.time.Clock()

# --------------------------------
# COLORS
# --------------------------------

WHITE = (248, 249, 252)
BLUE = (70, 100, 220)
DARK_BLUE = (45, 65, 160)
LIGHT_BLUE = (225, 232, 255)

GREEN = (55, 170, 90)
LIGHT_GREEN = (220, 245, 225)

RED = (210, 70, 70)
LIGHT_RED = (250, 225, 225)

BLACK = (35, 35, 45)
GRAY = (225, 227, 235)
DARK_GRAY = (100, 105, 120)

SHADOW = (210, 212, 220)

# --------------------------------
# FONTS
# --------------------------------

title_font = pygame.font.SysFont("Arial", 32, True)
heading_font = pygame.font.SysFont("Arial", 22, True)
font = pygame.font.SysFont("Arial", 18)
small_font = pygame.font.SysFont("Arial", 15)

# --------------------------------
# STACK
# --------------------------------

stack = []

input_text = ""
input_active = False

message = "Enter a value and choose an operation"
message_color = DARK_GRAY

# Animation
animation = ""
animation_start = 0


# --------------------------------
# DRAW TEXT
# --------------------------------

def draw_text(text, x, y, size=18, color=BLACK):

    f = pygame.font.SysFont("Arial", size)

    image = f.render(str(text), True, color)

    screen.blit(image, (x, y))


# --------------------------------
# DRAW ROUNDED BOX
# --------------------------------

def draw_box(x, y, width, height, color, radius=10):

    pygame.draw.rect(
        screen,
        color,
        (x, y, width, height),
        border_radius=radius
    )


# --------------------------------
# DRAW BUTTON
# --------------------------------

def draw_button(text, x, y, width, height):

    mouse_x, mouse_y = pygame.mouse.get_pos()

    hover = (
        x < mouse_x < x + width
        and
        y < mouse_y < y + height
    )

    # Shadow
    draw_box(
        x + 3,
        y + 4,
        width,
        height,
        SHADOW,
        10
    )

    if hover:
        color = DARK_BLUE
    else:
        color = BLUE

    draw_box(
        x,
        y,
        width,
        height,
        color,
        10
    )

    image = font.render(text, True, WHITE)

    text_x = x + (width - image.get_width()) // 2
    text_y = y + (height - image.get_height()) // 2

    screen.blit(image, (text_x, text_y))


# --------------------------------
# DRAW STACK
# --------------------------------

def draw_stack():

    # Stack base
    base_x = 310
    base_y = 565

    pygame.draw.line(
        screen,
        DARK_GRAY,
        (base_x, base_y),
        (base_x + 280, base_y),
        5
    )

    if len(stack) == 0:

        draw_text(
            "EMPTY",
            405,
            520,
            20,
            DARK_GRAY
        )

        return

    # Draw elements
    for i in range(len(stack)):

        value = stack[i]

        x = 310
        y = 510 - (i * 55)

        # Shadow
        draw_box(
            x + 4,
            y + 4,
            280,
            45,
            SHADOW,
            8
        )

        # Stack block
        draw_box(
            x,
            y,
            280,
            45,
            BLUE,
            8
        )

        # Value
        image = font.render(
            str(value),
            True,
            WHITE
        )

        text_x = x + (280 - image.get_width()) // 2

        screen.blit(
            image,
            (text_x, y + 11)
        )

    # TOP label
    top_y = 510 - ((len(stack) - 1) * 55)

    draw_text(
        "TOP",
        610,
        top_y + 12,
        15,
        GREEN
    )


# --------------------------------
# SHOW MESSAGE
# --------------------------------

def show_message(text, color):

    global message
    global message_color

    message = text
    message_color = color


# --------------------------------
# MAIN LOOP
# --------------------------------

running = True

while running:

    screen.fill(WHITE)

    # --------------------------------
    # HEADER
    # --------------------------------

    draw_text(
        "STACK VISUALISER",
        325,
        25,
        32,
        DARK_BLUE
    )

    draw_text(
        "LIFO - Last In, First Out",
        350,
        65,
        15,
        DARK_GRAY
    )

    # --------------------------------
    # INPUT SECTION
    # --------------------------------

    draw_text(
        "Enter Value",
        70,
        115,
        18,
        BLACK
    )

    # Input box shadow
    draw_box(
        180,
        108,
        380,
        50,
        SHADOW,
        8
    )

    # Input box
    if input_active:
        input_color = LIGHT_BLUE
        border_color = BLUE
    else:
        input_color = WHITE
        border_color = DARK_GRAY

    draw_box(
        180,
        105,
        380,
        50,
        input_color,
        8
    )

    pygame.draw.rect(
        screen,
        border_color,
        (180, 105, 380, 50),
        2,
        border_radius=8
    )

    draw_text(
        input_text,
        195,
        120,
        18,
        BLACK
    )

    # --------------------------------
    # STACK SIZE
    # --------------------------------

    draw_box(
        600,
        105,
        220,
        50,
        LIGHT_BLUE,
        10
    )

    draw_text(
        "Stack Size : " + str(len(stack)),
        630,
        120,
        18,
        DARK_BLUE
    )

    # --------------------------------
    # OPERATION BUTTONS
    # --------------------------------

    draw_text(
        "Operations",
        70,
        185,
        22,
        BLACK
    )

    draw_button(
        "PUSH",
        70,
        225,
        130,
        50
    )

    draw_button(
        "POP",
        215,
        225,
        130,
        50
    )

    draw_button(
        "PEEK",
        360,
        225,
        130,
        50
    )

    draw_button(
        "DISPLAY",
        505,
        225,
        130,
        50
    )

    draw_button(
        "IS EMPTY",
        650,
        225,
        130,
        50
    )

    # Clear button
    draw_button(
        "CLEAR",
        650,
        290,
        130,
        45
    )

    # --------------------------------
    # MESSAGE BOX
    # --------------------------------

    draw_box(
        70,
        300,
        540,
        55,
        GRAY,
        10
    )

    draw_text(
        message,
        90,
        318,
        16,
        message_color
    )

    # --------------------------------
    # STACK AREA
    # --------------------------------

    draw_text(
        "STACK",
        420,
        380,
        24,
        DARK_BLUE
    )

    draw_stack()

    # --------------------------------
    # EVENTS
    # --------------------------------

    for event in pygame.event.get():

        # CLOSE
        if event.type == pygame.QUIT:

            running = False

        # --------------------------------
        # KEYBOARD
        # --------------------------------

        if event.type == pygame.KEYDOWN:

            if input_active:

                if event.key == pygame.K_BACKSPACE:

                    input_text = input_text[:-1]

                elif event.key == pygame.K_RETURN:

                    input_active = False

                else:

                    # Only allow normal characters
                    if len(input_text) < 15:

                        input_text += event.unicode

        # --------------------------------
        # MOUSE
        # --------------------------------

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = pygame.mouse.get_pos()

            # --------------------------------
            # INPUT BOX
            # --------------------------------

            if (
                180 < mouse_x < 560
                and
                105 < mouse_y < 155
            ):

                input_active = True

            else:

                input_active = False

            # --------------------------------
            # PUSH
            # --------------------------------

            if (
                70 < mouse_x < 200
                and
                225 < mouse_y < 275
            ):

                if input_text != "":

                    stack.append(input_text)

                    show_message(
                        input_text + " pushed into stack",
                        GREEN
                    )

                    input_text = ""

                else:

                    show_message(
                        "Please enter a value",
                        RED
                    )

            # --------------------------------
            # POP
            # --------------------------------

            elif (
                215 < mouse_x < 345
                and
                225 < mouse_y < 275
            ):

                if len(stack) > 0:

                    value = stack.pop()

                    show_message(
                        value + " popped from stack",
                        GREEN
                    )

                else:

                    show_message(
                        "Stack Underflow - Stack is empty",
                        RED
                    )

            # --------------------------------
            # PEEK
            # --------------------------------

            elif (
                360 < mouse_x < 490
                and
                225 < mouse_y < 275
            ):

                if len(stack) > 0:

                    show_message(
                        "Top element = " + stack[-1],
                        GREEN
                    )

                else:

                    show_message(
                        "Stack is empty",
                        RED
                    )

            # --------------------------------
            # DISPLAY
            # --------------------------------

            elif (
                505 < mouse_x < 635
                and
                225 < mouse_y < 275
            ):

                if len(stack) > 0:

                    show_message(
                        "Stack = " + str(stack),
                        GREEN
                    )

                else:

                    show_message(
                        "Stack is empty",
                        RED
                    )

            # --------------------------------
            # IS EMPTY
            # --------------------------------

            elif (
                650 < mouse_x < 780
                and
                225 < mouse_y < 275
            ):

                if len(stack) == 0:

                    show_message(
                        "Stack is Empty",
                        RED
                    )

                else:

                    show_message(
                        "Stack is Not Empty",
                        GREEN
                    )

            # --------------------------------
            # CLEAR
            # --------------------------------

            elif (
                650 < mouse_x < 780
                and
                290 < mouse_y < 335
            ):

                stack.clear()

                show_message(
                    "Stack cleared successfully",
                    GREEN
                )

    # --------------------------------
    # UPDATE SCREEN
    # --------------------------------

    pygame.display.update()

    clock.tick(60)


pygame.quit()