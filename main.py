import pygame
import random

SCReen_Width = 800
SCReen_Height = 600

popal = 0
mimo = 0

pygame.init()

screen = pygame.display.set_mode((SCReen_Width, SCReen_Height))

pygame.display.set_caption("Игра тир")

target_imp = pygame.image.load("image/pixelcut-export.png")
target_width = target_imp.get_width()
target_height = target_imp.get_height()

t_x = random.randint(0, SCReen_Width - target_width)
t_y = random.randint(300, SCReen_Height - target_height)

paper = pygame.image.load("image/fon.jpg")
screen.blit(paper, (0, 0))

shrift = pygame.font.Font(None, 36)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if t_x <= x <= t_x + target_width and t_y < y <= t_y + target_height:
                popal+=1
            else:
                mimo+=1

            t_x = random.randint(0, SCReen_Width - target_width)
            t_y = random.randint(300, SCReen_Height - target_height)
            txt_object = shrift.render("Текущий счет: "+str(popal) + ":" + str(mimo)+"", True, (0, 32, 255))
            screen.blit(paper, (0, 0))
            screen.blit(target_imp, (t_x, t_y))
            screen.blit(txt_object, (10, 10))

    pygame.display.update()
pygame.quit()