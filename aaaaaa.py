import random

import pygame


# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the height and width of the screen
size = [600, 600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Drawing Rectangle")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# 글자체(text font) 지정하기
myFont = pygame.font.SysFont(None, 50)  # (글자체, 글자크기) None=기본글자체


# b=[]
# for j in range(0, 5):
#     for i in range(0, 5):
#         c = random.randint(1, 25)
#         while c in b:  # a가 이미 뽑은 리스트에 있을 때까지 다시 뽑자
#             c = random.randint(1, 25)
#         b.append(c)  #
#         b.sort()
screen.fill(WHITE)


for j in range(0, 5):

    for i in range(0, 5):
        d = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']
        # d = ['1', '2', '3', '4', '5', 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        random.shuffle(d)
        print(d[0])
        f=random.randrange(0,25)



        a = pygame.draw.rect(screen, BLACK, [50 + (i * 100), 10 + (j * 100), 100, 100], 1)
        # if b == 3:
        #     a = pygame.draw.rect(screen, BLACK, [50 + (i * 100), 10 + (j * 100), 100, 100])
        # else:
        #     a = pygame.draw.rect(screen, BLACK, [50 + (i * 100), 10 + (j * 100), 100, 100], 1)

        x = 50 + (i * 100)
        y = 10 + (j * 100)
        myFont = pygame.font.SysFont("arial", 20, True, False)
        if d[0] in d:
            text_Title = myFont.render(f'{d[0]}', True, BLACK)
        else:
            continue








        # Rect 생성

        text_Rect = text_Title.get_rect()

        text_Rect.x = x

        text_Rect.y = y

        # Text Surface SCREEN에 복사하기, Rect 사용

        screen.blit(text_Title, text_Rect)



screen.blit(text_Title, text_Rect)

while not done:


    clock.tick(10)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we a

    pygame.display.flip()

# Be IDLE friendly
pygame.quit()