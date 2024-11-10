import pygame
import sys


def win(mas, sign):
    zeroes = 0
    for row in mas:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return f'Победил {sign}!'
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return f'Победил {sign}!'
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return f'Победил {sign}!'
    if zeroes == 0:
        return 'Piece'
    return False


pygame.init()

size_block = 100
margin = 15
width = height = size_block * 3 + margin * 4

size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Tic-Tak-Toe")

black = (0, 0, 0)
ghost_white	= (248, 248, 255)
dark_slate_gray = (47, 79, 79)
white = (255, 255, 255)
pink = (255, 192, 203)
turquoise = (64, 224, 208)
mas = [[0] * 3 for i in range(3)]
query = 0
game_over = False
while True:
    screen.fill(dark_slate_gray)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (margin + size_block)
            row = y_mouse // (margin + size_block)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0
    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = pink
                elif mas[row][col] == 'o':
                    color = turquoise
                else:
                    color = white
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == pink:
                    light_cyan = (224, 255, 255)
                    pygame.draw.line(screen, light_cyan, (x + 5, y + 5), (size_block + x - 5, size_block + y - 5), 5)
                    pygame.draw.line(screen, light_cyan, (x + size_block - 5, y + 5), (x + 5, size_block + y - 5), 5)
                elif color == turquoise:
                    lavender = (230, 230, 250)
                    pygame.draw.circle(screen, lavender, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3,
                                       3)
    if (query - 1) % 2 == 0:
        game_over = win(mas, 'x')
    else:
        game_over = win(mas, 'o')

    if game_over:
        screen.fill(ghost_white)
        font = pygame.font.SysFont('stxingkai', 80)
        text = font.render(game_over, True, black)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])

    pygame.display.update()
