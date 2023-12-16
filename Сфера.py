import pygame

aaa = int(input())


pygame.init()

q = 40
e = 300

x = 136.5
y = 0

size = width, height = 300, 300
screen = pygame.display.set_mode(size)
pygame.draw.ellipse(screen, 'white', (0, 0, 300, 300), 1)

for i in range(1, aaa):
    pygame.draw.ellipse(screen, 'white', (x, y, q, e), 1)
    pygame.draw.ellipse(screen, 'white', (y, x, e, q), 1)
    q += 28
    x -= 15

    pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass

pygame.quit()