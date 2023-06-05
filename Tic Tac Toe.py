import random
import pygame
import sys
import numpy as np

pygame.init()

width = 600
height = 600

display = pygame.display.set_mode((width, height))
pygame.display.set_caption('TIC TAC TOE')
Line_color = (10, 0, 20)
colour = (140, 190, 190)
display.fill(colour)
cols = 3
rows = 3
board = np.zeros((rows, cols))


def draw_box():
    # horizontal line 1
    pygame.draw.line(display, Line_color, (0, 200), (600, 200), 10)
    # horizontal line 2
    pygame.draw.line(display, Line_color, (0, 400), (600, 400), 10)
    # vertical line 1
    pygame.draw.line(display, Line_color, (200, 0), (200, 600), 10)
    # vertical line 2
    pygame.draw.line(display, Line_color, (400, 0), (400, 600), 10)


def draw_board():
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 1:
                pygame.draw.circle(display, (255, 255, 255), (int(col * 200 + 100), int(row * 200 + 100)), 60, 10)
            elif board[row][col] == 2:
                pygame.draw.line(display, (255, 255, 255), (col * 200 + 55, row * 200 + 45),
                                 (col * 200 + 145, row * 200 + 155), 10)
                pygame.draw.line(display, (255, 255, 255), (col * 200 + 145, row * 200 + 45),
                                 (col * 200 + 55, row * 200 + 155), 10)


def board_space(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False


def board_full():
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 0:
                return False
    return True


def mark_board(row, col, player):
    board[row][col] = player


def check_win(player):
    # Check rows
    for row in range(rows):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True

    # Check columns
    for col in range(cols):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def reset_board():
    global board
    board = np.zeros((rows, cols))
    display.fill(colour)
    draw_box()


draw_box()

player = 1  # Player 1 starts

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and not check_win(player) and not board_full():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clicked_row = mouse_y // 200
            clicked_col = mouse_x // 200

            if board_space(clicked_row, clicked_col):
                mark_board(clicked_row, clicked_col, player)
                draw_board()

                if check_win(player):
                    print(f"Player {player} wins!")
                    reset_board()
                elif board_full():
                    print("It's a tie!")
                    reset_board()

                player = 3 - player  # Switch player (alternates between 1 and 2)

    pygame.display.update()
