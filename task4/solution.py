class TicTacToeBoard:
    def __init__(self):
        self.board = {'A1': ' ', 'A2': ' ', 'A3': ' ',
                      'B1': ' ', 'B2': ' ', 'B3': ' ',
                      'C1': ' ', 'C2': ' ', 'C3': ' '}
        self.last_move = None
        self.list_of_moves = ['X', 'O']

    def __setitem__(self, key, value):
        if key not in self.board:
            raise InvalidKey

        if value not in self.list_of_moves:
            raise InvalidValue

        if self.board[key] is not " ":
            raise InvalidMove

        if self.last_move == value:
            raise NotYourTurn

        self.board[key] = value
        self.last_move = value

    def __getitem__(self, key):
        return self.board[key]

    def __str__(self):
        return '\n  -------------\n' +\
            '3 | ' + self.board['A3'] + ' | ' + self.board['B3'] +\
            ' | ' + self.board['C3'] + ' |\n' +\
            '  -------------\n' +\
            '2 | ' + self.board['A2'] + ' | ' + self.board['B2'] +\
            ' | ' + self.board['C2'] + ' |\n' +\
            '  -------------\n' +\
            '1 | ' + self.board['A1'] + ' | ' + self.board['B1'] +\
            ' | ' + self.board['C1'] + ' |\n' +\
            '  -------------\n' +\
            '    A   B   C  \n'

    def combinations(self, z):
        self.wins = [[self.board['A1'], self.board['A2'], self.board['A3']],
                    [self.board['B1'], self.board['B2'], self.board['B3']],
                    [self.board['C1'], self.board['C2'], self.board['C3']],
                    [self.board['A1'], self.board['B1'], self.board['C1']],
                    [self.board['A2'], self.board['B2'], self.board['C2']],
                    [self.board['A3'], self.board['B3'], self.board['C3']],
                    [self.board['A1'], self.board['B2'], self.board['C3']],
                    [self.board['A3'], self.board['B2'], self.board['C3']]]

        for l in self.wins:
            if l[0] == l[1] == l[2] == z:
                return True

        return False

    def is_board_empty(self):
        positions = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        for p in positions:
            if self.board[p] == ' ':
                return True
        else:
                return False

    def game_status(self):
        if self.combinations('O'):
            return "O wins!"

        if self.combinations('X'):
            return "X wins!"

        if self.combinations('X') is self.combinations('O') is False:
            if self.is_board_empty():
                return "Game in progress."
            if self.is_board_empty() is False:
                return "Draw!"


class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidKey(Exception):
    pass


class NotYourTurn(Exception):
    pass
