import pygame

n = int(input())

w, h = 300, 300
coord_shift = n // 2

pygame.init()

screen = pygame.display.set_mode((w, h))

screen.fill(pygame.Color("yellow"))
color = pygame.Color("orange")

for x in range(coord_shift, w - coord_shift, coord_shift * 2):
    for y in range(coord_shift, h - coord_shift, coord_shift * 2):
        left, right = (x - coord_shift, y), (x + coord_shift, y)
        up, down = (x, y - coord_shift), (x, y + coord_shift)
        pygame.draw.polygon(screen, color, (left, up, right, down), 0)

pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass
