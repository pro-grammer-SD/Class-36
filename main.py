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
    else:
        color1 = (0, 255, 0)

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, color1, rect1)
    pygame.draw.rect(screen, (255, 0, 0), rect2)

    pygame.display.flip()
    clock.tick(60)
