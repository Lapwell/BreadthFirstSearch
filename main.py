import pygame
import sys

pygame.init()

WHITE = 255, 255, 255
BLACK = 0, 0, 0
GREY = 64, 64, 64
RED = 200, 0, 0
GREEN = 0, 200, 0
BLUE = 0, 0, 200

OFFSET = 2  # Offset is the thickness of the black lines.
SQR_SIZE = 20  # The size of the squares in the grid.
print("Enter 'n' for default value.\nLeft-click for walls, right-click for start, mousewheel-click for end.")
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


def mouse_click(square_type):
    global current_start
    global current_end
    for item in grid:
        if item.rect.collidepoint(pygame.mouse.get_pos()) and square_type == 'wall':
            if item.colour != WHITE:
                if item.colour == GREEN:
                    current_start = blank_square
                    print('green')
                elif item.colour == RED:
                    current_end = blank_square
                    print('red')
                else:
                    item.colour = WHITE
                    print('white')
                    continue
            item.colour = GREY
        elif item.rect.collidepoint(pygame.mouse.get_pos()) and square_type == 'start':
            if item.colour == RED:
                current_end = blank_square
            current_start.colour = WHITE
            item.colour = GREEN
            current_start = item
        elif item.rect.collidepoint(pygame.mouse.get_pos()) and square_type == 'end':
            if item.colour == GREEN:
                current_start = blank_square
            current_end.colour = WHITE
            item.colour = RED
            current_end = item


def fps_counter():
    count = str(int(clock.get_fps()))
    fps_txt = FONT.render(count, True, GREEN)
    ROOT.blit(fps_txt, (fps_txt.get_width() - fps_txt.get_width()//2, fps_txt.get_height() - fps_txt.get_height()//2))


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_focused() and event.button == 1:  # This statement is for placing the walls.
            mouse_click('wall')
        if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_focused() and event.button == 2:  # This is for placing the end square.
            mouse_click('end')
        if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_focused() and event.button == 3:  # This statement is for placing the start square.
            mouse_click('start')


def update_root():
    ROOT.fill(BLACK)
    for item in grid:
        pygame.draw.rect(ROOT, item.colour, item.rect)
    fps_counter()
    pygame.display.update()


grid_posx, grid_posy = OFFSET, OFFSET
if __name__ == "__main__":
    blank_square = GridSquare(0, 0, WHITE)
    current_start = blank_square  # This is to store where the start square is on the grid.
    current_end = blank_square  # This is to store the end square coords on the grid.
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
