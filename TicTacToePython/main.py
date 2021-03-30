import pygame
import sys
import math


from tictactoe_client import TicTacToeClient
from tictactoe_ai import TicTacToeAI


SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
CELL_SIZE = CELL_WIDTH, CELL_HEIGHT = int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/3)
MARK_SIZE = MARK_WIDTH, MARK_HEIGHT = int(CELL_WIDTH*0.8), int(CELL_HEIGHT*0.8)
IN_CELL_OFFSET = IN_CELL_OFFSET_WIDTH, IN_CELL_OFFSET_HEIGHT = int((CELL_WIDTH-MARK_WIDTH)/2), int((CELL_HEIGHT-MARK_HEIGHT)/2)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


def _translate_to_screen_coords(coords):
    return coords[0] * CELL_WIDTH + IN_CELL_OFFSET_WIDTH, coords[1] * CELL_HEIGHT + IN_CELL_OFFSET_HEIGHT


if __name__ == '__main__':
    # Set up display
    pygame.display.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    mark_x = pygame.Surface(MARK_SIZE)
    pygame.draw.line(mark_x, BLUE, (0, 0), (MARK_WIDTH, MARK_HEIGHT), 10)
    pygame.draw.line(mark_x, BLUE, (0, MARK_HEIGHT), (MARK_WIDTH, 0), 10)

    mark_o = pygame.Surface(MARK_SIZE)
    pygame.draw.circle(mark_o, RED, (int(MARK_WIDTH/2), int(MARK_HEIGHT/2)), MARK_WIDTH/2, 10)

    player_mark = {
        1: mark_x,
        2: mark_o
    }

    # Set up board
    pygame.draw.line(screen, WHITE, (int(SCREEN_WIDTH/3), 0), (int(SCREEN_WIDTH/3), SCREEN_HEIGHT))
    pygame.draw.line(screen, WHITE, (int(SCREEN_WIDTH/3)*2, 0), (int(SCREEN_WIDTH/3)*2, SCREEN_HEIGHT))
    pygame.draw.line(screen, WHITE, (0, int(SCREEN_HEIGHT/3)), (SCREEN_WIDTH, int(SCREEN_HEIGHT/3)))
    pygame.draw.line(screen, WHITE, (0, int(SCREEN_HEIGHT/3)*2), (SCREEN_WIDTH, int(SCREEN_HEIGHT/3)*2))
    
    # Draw screen
    pygame.display.flip()

    is_ai_turn = False
    is_ended = False

    # Initialize backend
    game_client = TicTacToeClient(first_player=1)
    game_ai = TicTacToeAI(ai_id=2, game_object=game_client)


    # Main game loop
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.constants.QUIT:
                sys.exit()
            elif event.type == pygame.constants.MOUSEBUTTONUP:
                if not is_ai_turn and not is_ended:
                    cursor_position = pygame.mouse.get_pos()
                    coords = math.floor(cursor_position[0]/CELL_SIZE[0]), math.floor(cursor_position[1]/CELL_SIZE[1])
                    player_coord = game_client.move(player_id=1, coord=coords)
                    draw_coords = _translate_to_screen_coords(player_coord)
                    screen.blit(player_mark[1], draw_coords)
                    is_ai_turn = True
                    is_ended = game_client.is_ended()

        if is_ai_turn and not is_ended:
            ai_coord = game_ai.move()
            draw_coords = _translate_to_screen_coords(ai_coord)
            screen.blit(player_mark[2], draw_coords)
            is_ai_turn=False
            is_ended = game_client.is_ended()
        
        pygame.display.flip()
