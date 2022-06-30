import pygame,sys

pygame.init()
clock = pygame.time.Clock()

# game screen
screen_width = 612  # 128 * 4
screen_height = 421  # 64 * 4
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("graphics/bg.jpg")
pygame.display.set_caption("Four Leaf")

# files
leaf_images = {
    "egg" : ["graphics/4_leaf/egg_sprite_01.png", "graphics/4_leaf/egg_cracking_01.png", "graphics/4_leaf/egg_cracking_02.png",
       "graphics/4_leaf/egg_cracking_03.png","graphics/4_leaf/egg_cracking_04.png"],

    "leaf_left" : ["graphics/4_leaf/left.png", "graphics/4_leaf/step_left_1.png",
        "graphics/4_leaf/step_left_2.png"],

    "leaf_right" : ["graphics/4_leaf/right.png", "graphics/4_leaf/step_right_1.png",
        "graphics/4_leaf/step_right_2.png"],

    "leaf_happy_left" : ["graphics/4_Leaf/happy_left.png", "graphics/4_Leaf/happy_step_left_1.png",
              "graphics/4_leaf/happy_step_left_2.png"],
    "leaf_happy_right" : ["graphics/4_Leaf/happy_right.png", "graphics/4_Leaf/happy_step_right_1.png",
              "graphics/4_leaf/happy_step_right_2.png"],

    "leaf_sad_left" : ["graphics/4_leaf/sad_left.png", "graphics/4_leaf/sad_step_left_1.png",
            "graphics/4_leaf/sad_step_left_2.png"],
    "leaf_sad_right" : ["graphics/4_leaf/sad_right.png", "graphics/4_leaf/sad_step_right_1.png",
            "graphics/4_leaf/sad_step_right_2.png"]
}

class ToolBar(pygame.sprite.Sprite):
    def __init__(self, image_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]


# creating toolbar
tb_group = pygame.sprite.Group()

toolbar_a = ["graphics/toolbar/book.png", "graphics/toolbar/call.png", "graphics/toolbar/firstaid.png",
             "graphics/toolbar/food.png"]
toolbar_b = ["graphics/toolbar/game.png", "graphics/toolbar/heart.png", "graphics/toolbar/lightbulb.png",
             "graphics/toolbar/toilet.png"]
x = 50
y = 10
for tb in toolbar_a[:]:
    tb_icon = ToolBar(tb, x, y)
    x += 150
    tb_group.add(tb_icon)
x = 50
y = 350
for tb in toolbar_b[:]:
    tb_icon = ToolBar(tb, x, y)
    x += 150
    tb_group.add(tb_icon)

# System fonts
font = pygame.font.SysFont("Comic Sans MS", 36)
text = font.render("Hi, I'm Four Leaf" , True, 'black')
run = True

# leafs animations
pos_x = 100
pos_y = 200
step = True
left = False

while run:
    for event in pygame.event.get():  # pygame.display.update()
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

    if left == False:
        if pos_x <= 400:
            pos_x = pos_x + 10
            print("+")
        else:
            left = True
            print("True")
    if left == True:
        if pos_x >= 20:
            pos_x = pos_x - 10
            print("-")
        else:
            left = False
            print("False")
    if step:
        if left == True:
            leaf_animation = (leaf_images["leaf_left"][2])
        else:
            leaf_animation = (leaf_images["leaf_right"][2])
        step = False
    else:
        if left == True:
            leaf_animation = (leaf_images["leaf_left"][1])
        else:
            leaf_animation = (leaf_images["leaf_right"][1])
        step = True

    leaf = pygame.image.load(leaf_animation)

    screen.blit(background, (0, 0))
    screen.blit(leaf, (pos_x,pos_y))
    screen.blit(text, (150, 120))
    tb_group.draw(screen)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(3)

