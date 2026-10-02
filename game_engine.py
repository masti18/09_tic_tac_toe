"""Game state, move validation, scoring, and round control."""

import pygame

from game.ai import choose_move
from game.renderer import board_pos_to_cell
from game.rules import check_winner, is_board_full

HUMAN_SYMBOL = "X"
COMPUTER_SYMBOL = "O"


class GameEngine:
    def __init__(self):
        self.x_wins = 0
        self.o_wins = 0
        self.draws = 0
        self.first_player = HUMAN_SYMBOL
        self._start_round()

    def _start_round(self):
        self.board = [[None] * 3 for _ in range(3)]
        self.current_player = self.first_player
        self.round_over = False
        self.winner = None
        self._maybe_take_computer_turn()

    def restart_round(self):
        """Restart only the current round; preserve the scoreboard."""
        self._start_round()

    def reset_match(self):
        """Reset both the current round and all match scores."""
        self.x_wins = 0
        self.o_wins = 0
        self.draws = 0
        self._start_round()

    def set_first_player(self, symbol):
        if symbol not in (HUMAN_SYMBOL, COMPUTER_SYMBOL):
            return
        self.first_player = symbol

    def handle_click(self, pos):
        # Ignore clicks after a round ends or while the computer is moving.
        if self.round_over or self.current_player != HUMAN_SYMBOL:
            return

        cell = board_pos_to_cell(pos)
        if cell is None:
            return

        row, col = cell
        # Reject occupied cells without changing the board or turn.
        if self.board[row][col] is not None:
            return

        self.board[row][col] = HUMAN_SYMBOL
        self.check_round_end()
        if self.round_over:
            return

        self.current_player = COMPUTER_SYMBOL
        self._maybe_take_computer_turn()

    def _maybe_take_computer_turn(self):
        if self.round_over or self.current_player != COMPUTER_SYMBOL:
            return

        move = choose_move(self.board)
        if move is None:
            self.check_round_end()
            return

        row, col = move
        self.board[row][col] = COMPUTER_SYMBOL
        self.check_round_end()
        if not self.round_over:
            self.current_player = HUMAN_SYMBOL

    def handle_keydown(self, key):
        if key == pygame.K_r:
            self.restart_round()
        elif key == pygame.K_m:
            self.reset_match()
        elif key == pygame.K_x:
            self.set_first_player(HUMAN_SYMBOL)
        elif key == pygame.K_o:
            self.set_first_player(COMPUTER_SYMBOL)
            # If no round has started yet, O will take the next move when restarted.

    def check_round_end(self):
        # Winner must be checked BEFORE full-board/draw detection.
        winner = check_winner(self.board)
        if winner:
            self.round_over = True
            self.winner = winner
            if winner == HUMAN_SYMBOL:
                self.x_wins += 1
            else:
                self.o_wins += 1
            return

        if is_board_full(self.board):
            self.round_over = True
            self.winner = None
            self.draws += 1

    def draw(self, surface, font):
        from game import renderer

        renderer.draw_board(surface, self.board)
        renderer.draw_scoreboard(
            surface,
            font,
            self.x_wins,
            self.o_wins,
            self.draws,
            self.first_player,
        )

        if self.round_over:
            text = f"{self.winner} wins!" if self.winner else "Draw!"
            renderer.draw_banner(surface, font, text)
        else:
            turn_label = (
                "Your turn (X)"
                if self.current_player == HUMAN_SYMBOL
                else "Computer's turn (O)"
            )
            renderer.draw_text(surface, font, turn_label, (10, 58))
