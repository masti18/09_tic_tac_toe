"""All Pygame drawing for the Tic-Tac-Toe game."""

import pygame

WIDTH, HEIGHT = 560, 560
BOARD_SIZE = 360
CELL_SIZE = BOARD_SIZE // 3
BOARD_LEFT = 100
BOARD_TOP = 125
WINDOW_SIZE = (WIDTH, HEIGHT)

COLOR_BG = (245, 245, 245)
COLOR_LINE = (60, 60, 60)
COLOR_X = (200, 60, 60)
COLOR_O = (60, 100, 200)
COLOR_TEXT = (30, 30, 30)
COLOR_PANEL = (225, 225, 225)


def board_pos_to_cell(pos):
    x, y = pos
    x -= BOARD_LEFT
    y -= BOARD_TOP
    if not (0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE):
        return None
    return int(y // CELL_SIZE), int(x // CELL_SIZE)


def draw_board(surface, board):
    surface.fill(COLOR_BG)
    for i in range(1, 3):
        pygame.draw.line(
            surface,
            COLOR_LINE,
            (BOARD_LEFT + i * CELL_SIZE, BOARD_TOP),
            (BOARD_LEFT + i * CELL_SIZE, BOARD_TOP + BOARD_SIZE),
            3,
        )
        pygame.draw.line(
            surface,
            COLOR_LINE,
            (BOARD_LEFT, BOARD_TOP + i * CELL_SIZE),
            (BOARD_LEFT + BOARD_SIZE, BOARD_TOP + i * CELL_SIZE),
            3,
        )

    for r in range(3):
        for c in range(3):
            symbol = board[r][c]
            if symbol is None:
                continue
            center = (
                BOARD_LEFT + c * CELL_SIZE + CELL_SIZE // 2,
                BOARD_TOP + r * CELL_SIZE + CELL_SIZE // 2,
            )
            if symbol == "X":
                offset = CELL_SIZE // 3
                pygame.draw.line(
                    surface, COLOR_X,
                    (center[0] - offset, center[1] - offset),
                    (center[0] + offset, center[1] + offset), 6,
                )
                pygame.draw.line(
                    surface, COLOR_X,
                    (center[0] + offset, center[1] - offset),
                    (center[0] - offset, center[1] + offset), 6,
                )
            else:
                pygame.draw.circle(surface, COLOR_O, center, CELL_SIZE // 3, 6)


def draw_text(surface, font, text, pos, color=COLOR_TEXT):
    surface.blit(font.render(text, True, color), pos)


def draw_scoreboard(surface, font, x_wins, o_wins, draws, first_player):
    pygame.draw.rect(surface, COLOR_PANEL, (0, 0, WIDTH, 48))
    draw_text(
        surface,
        font,
        f"X: {x_wins}    O: {o_wins}    Draws: {draws}",
        (10, 8),
    )
    draw_text(
        surface,
        font,
        f"First: {first_player}    [X/O] choose first | [R] round | [M] match",
        (10, 34),
    )


def draw_banner(surface, font, text):
    surf = font.render(text, True, (180, 40, 40))
    rect = surf.get_rect(center=(WIDTH // 2, BOARD_TOP + BOARD_SIZE + 25))
    surface.blit(surf, rect)
