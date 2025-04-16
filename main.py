import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Collision")

clock = pygame.time.Clock()

rect1 = pygame.Rect(100, 100, 50, 50)
rect2 = pygame.Rect(300, 300, 50, 50)

speed = 5
color1 = (0, 255, 0)

FONT_SIZE = 30
font = pygame.font.SysFont("Bai Jamjuree", FONT_SIZE) # other fonts works if they are load locally or installed
win_text = font.render("You win! \\(*°▽°*)/", True, pygame.Color('white'))

rt = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect1.x -= speed
    if keys[pygame.K_RIGHT]:
        rect1.x += speed
    if keys[pygame.K_UP]:
        rect1.y -= speed
    if keys[pygame.K_DOWN]:
        rect1.y += speed

    if rect1.colliderect(rect2):
        color1 = (255, 255, 0)
        rt = True
    else:
        color1 = (0, 255, 0)
        rt = False

    screen.fill((100,160,210))
    pygame.draw.rect(screen, color1, rect1)
    pygame.draw.rect(screen, (255, 0, 0), rect2)

    if rt:
        screen.blit(win_text, (10,10))
        pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
    