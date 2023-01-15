'''
Author: Naor Or-Zion
Date: 1/8/2023

A simple connect four game with GUI.
'''
import sys

import pygame
from sys import exit
from tkinter import *
from tkinter import messagebox

pygame.init()
screen = pygame.display.set_mode((1034, 944))
pygame.display.set_caption('Connect Four')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)
Tk().wm_withdraw()  # To hide the main window
player_turn = 1
score = 0

# Create a 2D list of tiles to represent the grid
tiles = [[0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]]

# Create a white surface the size of the board
surface = pygame.Surface((1034, 944))
surface.fill('White')

# Take the board and play pieces image and make a surface later on
board_image = pygame.image.load('connect4_board.png')
black_piece = pygame.image.load('black_piece.png')
red_piece = pygame.image.load('red_piece.png')

# Make a text surface using the font I created
score_label = font.render('Your Score: ', True, 'Black')
score_number = font.render('0', True, 'Black')


def reset_game():
    global score, tiles

    score = 0
    tiles = [[0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]

    render_surface()


def render_surface():
    # Which surface to display on screen, and where to place it.
    # Notice that the first "screen.blit()" call is the lowest layer of all surfaces

    # Constant surfaces
    screen.blit(surface, (0, 0))
    screen.blit(score_label, (1150, 60))
    screen.blit(board_image, (0, 0))

    draw_all_pieces()


def determine_piece(event):
    if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        x_pos = pos[0]
        y_pos = pos[1]

        if 0 <= x_pos <= 153:
            place_piece(0)
        if 153 < x_pos <= 299:
            place_piece(1)
        if 299 < x_pos <= 444:
            place_piece(2)
        if 444 < x_pos <= 590:
            place_piece(3)
        if 590 < x_pos <= 736:
            place_piece(4)
        if 736 < x_pos <= 881:
            place_piece(5)
        if 881 < x_pos <= 1025:
            place_piece(6)

        render_surface()

        if is_draw():
            pygame.display.flip()
            draw_message()
            reset_game()

        if is_win():
            pygame.display.flip()
            won_message()
            reset_game()


def place_piece(position):
    # player_turn and current_place can be:
    # 0 - No one
    # 1 - Black Piece
    # 2 - White Piece

    global player_turn

    player_turn = 1 if player_turn == 2 else 2

    for index, current_place in enumerate(tiles[position]):
        if current_place != 0 and index == 5:
            player_turn = 1 if player_turn == 2 else 2
            break
        if current_place == 0:
            tiles[position][index] = player_turn
            break


def draw_all_pieces():
    space_x = 146
    space_y = 142

    for x in range(len(tiles)):
        for y in range(len(tiles[x])):
            if tiles[x][y] == 1:
                screen.blit(black_piece, (11 + (space_x * x), 727 - (space_y * y)))
            elif tiles[x][y] == 2:
                screen.blit(red_piece, (11 + (space_x * x), 727 - (space_y * y)))


def draw_message():
    messagebox.showinfo('DRAW!', 'Come on people you are better than that...')


def won_message():
    if player_turn == 1:
        messagebox.showinfo('WIN!', 'BLACK WON - RED IS A LOSER')
    if player_turn == 2:
        messagebox.showinfo('WIN!', 'RED WON - BLACK IS A LOSER')


def is_draw():
    for row in tiles:
        for column in row:
            if column == 0:
                return False

    # No empty places found - returns False
    return True


def is_win():
    # Check rows
    for row in tiles:
        for i in range(4):
            if row[i] != 0 and row[i] == row[i + 1] == row[i + 2] == row[i + 3]:
                return True

    # Check columns
    for col in range(6):
        for i in range(3):
            if tiles[i][col] != 0 and tiles[i][col] == tiles[i + 1][col] == tiles[i + 2][col] == tiles[i + 3][col]:
                return True

    # Check diagonals
    for row in range(2):
        for col in range(3):
            if tiles[row][col] != 0 and tiles[row][col] == tiles[row + 1][col + 1] == tiles[row + 2][col + 2] == \
                    tiles[row + 3][col + 3]:
                return True
            if tiles[row][5 - col] != 0 and tiles[row][5 - col] == tiles[row + 1][4 - col] == tiles[row + 2][3 - col] == \
                    tiles[row + 3][2 - col]:
                return True

    # No winning configuration found
    return False


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

            render_surface()
            determine_piece(event)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()

'''
Documentation:

This script is a game of Connect Four. It uses Pygame to render the game board and handle player input.

The game begins by initializing Pygame and setting up the game window with a set size and caption. The clock and font variables are also initialized. The player_turn variable keeps track of which player's turn it is, with 1 representing the first player and 2 representing the second player. The score variable keeps track of the current score.

A 2D list called "tiles" is created to represent the game grid. It is initialized with all 0's, which represent empty tiles.

A white surface called "surface" is created and filled with the color white. It will be used as the background for the game board.

The "board_image" and "black_piece" and "red_piece" variables are created by loading image files. These will be used to render the game board and game pieces on the screen.

The "score_label" and "score_number" variables are created using the font that was previously initialized. They will be used to display the current score on the screen.

The "render_surface" function is responsible for rendering all of the surfaces (images) on the screen. It does this by using the "blit" method of the "screen" object to draw the "surface", "score_label", "board_image", and "calc_score" surfaces on the screen. The "draw_all_pieces" function is also called to render all of the game pieces on the screen.

The "determine_piece" function is called when a player clicks on the game board. It uses the "get_pos" method of the "pygame.mouse" object to get the position of the mouse click, and then determines which column the click occurred in. It then calls the "place_piece" function to place a game piece in that column. Finally, it calls the "render_surface" function to update the screen.

The "place_piece" function is responsible for placing a game piece in the specified column. It does this by looping through the specified column of the "tiles" list and finding the first empty tile (0). It then places the game piece (1 or 2) in that tile and updates the player_turn variable.

The "draw_all_pieces" function is responsible for rendering all of the game pieces on the screen. It does this by looping through the "tiles" list and drawing a black piece or red piece on the screen for each non-empty tile. The position of each piece is calculated using the "space_x" and "space_y" variables.

Finally, the main game loop is entered. The game listens for player input (mouse clicks) and redraws the screen whenever the player clicks on the game board. The loop runs at 60 frames per second, as specified by the "clock.tick" function.
'''
