import pygame
import sys
import os

# Constants
WIDTH, HEIGHT = 600, 600
BOARD_SIZE = 400
BORDER_SIZE = (WIDTH - BOARD_SIZE) // 2
ROWS, COLS = 8, 8
SQUARE_SIZE = BOARD_SIZE // COLS
OUTLINE_SIZE = 2  # The thickness of the outline

# Colors
OFF_WHITE = (240, 240, 230)
LIGHT_BLUE = (139, 69, 19)

# Chessboard representation
board = [
   ["black_rook.png", "black_knight.png", "black_bishop.png", "black_queen.png", "black_king.png", "black_bishop.png", "black_knight.png", "black_rook.png"],
   ["black_pawn.png", "black_pawn.png", "black_pawn.png", "black_pawn.png", "black_pawn.png", "black_pawn.png", "black_pawn.png", "black_pawn.png"],
   ["", "", "", "", "", "", "", ""],
   ["", "", "", "", "", "", "", ""],
   ["", "", "", "", "", "", "", ""],
   ["", "", "", "", "", "", "", ""],
   ["white_pawn.png", "white_pawn.png", "white_pawn.png", "white_pawn.png", "white_pawn.png", "white_pawn.png", "white_pawn.png", "white_pawn.png"],
   ["white_rook.png", "white_knight.png", "white_bishop.png", "white_queen.png", "white_king.png", "white_bishop.png", "white_knight.png", "white_rook.png"],
]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Load chess piece images
piece_images = {}
for row in range(ROWS):
   for col in range(COLS):
       piece_name = board[row][col]
       if piece_name:
           piece_images[piece_name] = pygame.image.load(os.path.join("pieces", piece_name)).convert_alpha()

def draw_board():
   for row in range(ROWS):
       for col in range(COLS):
           color = OFF_WHITE if (row + col) % 2 == 0 else LIGHT_BLUE
           pygame.draw.rect(screen, color, (BORDER_SIZE + col * SQUARE_SIZE, BORDER_SIZE + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
           piece_name = board[row][col]
           if piece_name:
               piece_image = piece_images[piece_name]
               piece_image = pygame.transform.scale(piece_image, (SQUARE_SIZE, SQUARE_SIZE))
               screen.blit(piece_image, (BORDER_SIZE + col * SQUARE_SIZE, BORDER_SIZE + row * SQUARE_SIZE))

def get_row_col_from_mouse(pos):
   x, y = pos
   row = (y - BORDER_SIZE) // SQUARE_SIZE
   col = (x - BORDER_SIZE) // SQUARE_SIZE
   return row, col

def is_valid_move(start_row, start_col, end_row, end_col):
   # Add logic for each of the pieces to ensure they can move correctly
   return True

def main():
   selected_piece = None
   while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           elif event.type == pygame.MOUSEBUTTONDOWN:
               mouse_pos = pygame.mouse.get_pos()
               row, col = get_row_col_from_mouse(mouse_pos)
               piece_name = board[row][col]

               if selected_piece is None:
                   if piece_name:
                       selected_piece = (row, col)
               else:
                   if is_valid_move(selected_piece[0], selected_piece[1], row, col):
                       # Move the piece
                       board[row][col] = board[selected_piece[0]][selected_piece[1]]
                       board[selected_piece[0]][selected_piece[1]] = ""
                   selected_piece = None

       screen.fill(OFF_WHITE)  # Fill the screen with off-white color
       pygame.draw.rect(screen, LIGHT_BLUE, (BORDER_SIZE - OUTLINE_SIZE, BORDER_SIZE - OUTLINE_SIZE, BOARD_SIZE + 2 * OUTLINE_SIZE, BOARD_SIZE + 2 * OUTLINE_SIZE))  # Draw the outline
       pygame.draw.rect(screen, LIGHT_BLUE, (BORDER_SIZE, BORDER_SIZE, BOARD_SIZE, BOARD_SIZE))  # Draw the chessboard border
       draw_board()
       pygame.display.update()

if __name__ == "__main__":
   main()

