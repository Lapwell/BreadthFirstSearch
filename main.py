import pygame
import sys

pygame.init()

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

WIDTH, HEIGHT = 800, 800
ROOT = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pygame.time.Clock()
FONT = pygame.font.Font(None, 24)

wsize, hsize = WIDTH // 20, HEIGHT // 20
row_size, column_size = WIDTH // wsize, HEIGHT // hsize
grid_square = pygame.Rect(0, 0, wsize, hsize)
grid = []


def fps_counter():
    count = str(int(clock.get_fps()))
    fps_txt = FONT.render(count, True, WHITE)
    ROOT.blit(fps_txt, (fps_txt.get_width() - fps_txt.get_width()//2, fps_txt.get_height() - fps_txt.get_height()//2))


def check_events():
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def update_root():
    ROOT.fill(BLACK)
    fps_counter()
    pygame.display.update()


def main():
    check_events()
    update_root()
    clock.tick(FPS)


if __name__ == "__main__":
    while True:
        main()
