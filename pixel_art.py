import pygame
# import math

pygame.font.init()

rez = 20
width = 600
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pixel Art')

line_x = width // 28
line_y = height // 28

def get_rect_pos():
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    return (x - (x % rez), y - (y % rez), rez, rez)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(display, (255, 255, 255), get_rect_pos())
                # print(get_mouse_pos())

            for i in range(1, int(width / rez)):
                pygame.draw.line(display, (255, 255, 255), (i * rez, 0), (i * rez, width))

            for j in range(1, int(height / rez)):
                pygame.draw.line(display, (255, 255, 255), (0, j * rez), (height, j * rez))

        pygame.display.flip()
main()
