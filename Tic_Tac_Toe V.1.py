import random
from turtle import color 
import pygame
import sys
import numpy as np

pygame.init()

width = 600
height = 600

display = pygame.display.set_mode((width,height))
pygame.display.set_caption('TIC TAC TOE')
Line_color = (10,0,20)
colour = (140,190,190)
display.fill(colour)
cols = 3
rows = 3
board = np.zeros((rows,cols))

def draw_box():
    
    # horizontal line 1
    pygame.draw.line(display ,Line_color,(0,200),(600,200),10)
    # horizontal line 2
    pygame.draw.line(display ,Line_color,(0,400),(600,400),10)
    # vertical line 1
    pygame.draw.line(display ,Line_color,(200,0),(200,600),10)
    # vertical line 2
    pygame.draw.line(display ,Line_color,(400,0),(400,600),10)

draw_box()

def board_space(row,col):

    if board[row][col] == 0:
        return True
    else:
        return False



def board_full():

    for row in range(rows):
        for col in range(cols):
            if board[row][col]==0:
                return False

    return True 

# Test
print(board)
print(board_space(0,0))
print(board_full())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()


