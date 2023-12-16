import pygame

run = True

size = w, h = 300, 200

brick_size = 30, 15

wh_line = 2
ran = 15

pygame.init()

screen = pygame.display.set_mode(size)

screen.fill((255, 255, 255))

for i in range(0, size[1], brick_size[1] + wh_line):
    for j in range(-ran, size[0], brick_size[0] + wh_line):
        if (i + brick_size[1] + wh_line) // (brick_size[1] + wh_line) % 2 == 0:
            j += ran
        pygame.draw.rect(screen, 'red', (j, size[1] - i - brick_size[1], brick_size[0], brick_size[1]))

pygame.display.flip()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()