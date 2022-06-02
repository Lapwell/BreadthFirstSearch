import pygame
import sys

pygame.init()

WHITE = 255, 255, 255
BLACK = 0, 0, 0
GREY = 64, 64, 64
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

OFFSET = 2  # Offset is the thickness of the black lines.
SQR_SIZE = 20  # The size of the squares in the grid.
# print("Enter 'n' for default value.")
# X_SQUARES, Y_SQUARES = input('Input X amount:'), input("Input Y amount:")  # The amount of squares in the x-axis and y-axis.
X_SQUARES, Y_SQUARES = 'n', 'n'
if X_SQUARES or Y_SQUARES == 'n':
    X_SQUARES, Y_SQUARES = 40, 40


WIDTH, HEIGHT = (X_SQUARES * OFFSET) + (SQR_SIZE * X_SQUARES) + OFFSET, (Y_SQUARES * OFFSET) + (SQR_SIZE * Y_SQUARES) + OFFSET
ROOT = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
FPS = 60
clock = pygame.time.Clock()
FONT = pygame.font.Font(None, 24)

grid = []  # This list is for the grid of squares to be stored in.


class GridSquare:
    def __init__(self, posx, posy, colour):
        self.colour = colour
        self.rect = pygame.Rect(posx, posy, SQR_SIZE, SQR_SIZE)


def mouse_click():
    for item in grid:
        if item.rect.collidepoint(pygame.mouse.get_pos()):
            item.colour = GREY
            print('Collide true', pygame.mouse.get_pos())


def fps_counter():
    count = str(int(clock.get_fps()))
    fps_txt = FONT.render(count, True, GREEN)
    ROOT.blit(fps_txt, (fps_txt.get_width() - fps_txt.get_width()//2, fps_txt.get_height() - fps_txt.get_height()//2))


def check_events():
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_focused() and event.button == 1:
            mouse_click()


def update_root():
    ROOT.fill(BLACK)
    for item in grid:
        pygame.draw.rect(ROOT, item.colour, item.rect)
    fps_counter()
    pygame.display.update()


grid_posx, grid_posy = OFFSET, OFFSET
if __name__ == "__main__":
    for i in range(0, Y_SQUARES):
        for y in range(0, X_SQUARES):
            grid.append(GridSquare(grid_posx, grid_posy, WHITE))
            grid_posx += SQR_SIZE + OFFSET
        grid_posy += SQR_SIZE + OFFSET
        grid_posx = OFFSET
    while True:
        check_events()
        update_root()
        clock.tick(FPS)
