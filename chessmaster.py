#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A simple chess game module."""

import time


class ChessPiece(object):
    """A class that records chess moves.

    Attributes:
        prefix (str): Supposed to be a prefix that represents each chess piece.
                      Defaults to an empty string.
    """
    prefix = ''

    def __init__(self, position):
        """Constructor for ChessPiece class.

        Args:
            position (str): the tile notation of starting position.

        Attributes:
            position (str): the tile notation of starting position.
            moves (list): a list that stores moves history with timestamp.

        Raises:
            ValueError: If position is not a valid tile on the gameboard.
        """
        self.position = position
        self.moves = []
        if self.is_legal_move(position) is False:
            excep = '`{0}` is not a legal start position'
            raise ValueError(excep.format(position))

    def algebraic_to_numeric(self, tile):
        """A function to convert the tile names into a numeric tuple.

        Args:
            tile (str): The algebraic notation of the position of the piece.

        Returns:
            tuple: A 2 value tuple with 0-based x and y-coordinate.
            None: It returns None if invalid coordinate is passed.
                  Shell may not print out None.

        Examples:
            >>> algebraic_to_numeric('a1')
            >>> (0, 0)

            >>> algebraic_to_numeric('g8')
            >>> (6, 7)
        """
        alpha = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
        num = ('1', '2', '3', '4', '5', '6', '7', '8')

        if tile[0] in alpha and tile[1] in num:
            y_axis = alpha.index(tile[0])
            x_axis = num.index(tile[1])
            return (y_axis, x_axis)
        else:
            return None

    def is_legal_move(self, position):
        """Test if the position is legal.

        Args:
            position (str): The algebraic notation of the new position of the
                            piece.

        Returns:
            bool: True, if legal when tested in algebraic_to_numeric().
                  Else False.

        Examples:
            >>> mo = ChessPiece('a1')
            >>> mo.is_legal_move('a1')
            True
            >>> mo.is_legal_move('j1')
            False
        """
        if self.algebraic_to_numeric(position):
            return True
        else:
            return False

    def move(self, position):
        """Function that moves the piece to a new position.

        Args:
            position (str): The algebraic notation of the new position.

        Returns:
            tuple: A tuple that includes the old position, the new position,
                   and the timestamp of the move. If the move is not legal,
                   returns False.

        Examples:
            >>> mo = ChessPiece('a1')
            >>> mo.move('g4')
            ('a1', 'g4', 1478322673.462096)
            >>> mo.move('j3')
            False
        """
        oldposition = self.prefix + self.position
        if self.is_legal_move(position):
            self.position = position
            newposition = self.prefix + position
            timestamp = time.time()
            record = (oldposition, newposition, timestamp)
            self.moves.append(record)
            return record
        else:
            return False


class Rook(ChessPiece):
    """A subclass of ChessPiece, for Rook.

    Attributes:
        prefix (str): Represents the Rook pieces.
    """
    prefix = 'R'

    def __init__(self, position):
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """Test if the move is legal.

        Args:
            position (str): The algebraic notation of the new position of the
                            piece.

        Returns:
            bool: True, if legal. Else False.

        Examples:
            >>> ro = Rook('a1')
            >>> ro.prefix
            'R'
            >>> ro.move('b2')
            False
            >>> ro.move('h1')
            ('Ra1', 'Rh1', 1478410084.336379)
            >>> ro.move('h8')
            ('Rh1', 'Rh8', 1478410116.604157)
        """
        if self.position[0] == position[0] or self.position[1] == position[1]:
            return True
        else:
            return False


class Bishop(ChessPiece):
    """A subclass of ChessPiece, for Bishop.

    Attributes:
        prefix (str): Represents the Bishop pieces.
    """
    prefix = 'B'

    def __init__(self, position):
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """Test if the move is legal.

        Args:
            position (str): The algebraic notation of the new position of the
                            piece.

        Returns:
            bool: True, if legal. Else False.

        Examples:
            >>> bi = Bishop('a1')
            >>> bi.prefix
            'B'
            >>> bi.move('a2')
            False
            >>> bi.move('c3')
            ('Ba1', 'Bc3', 1478409908.028589)
            >>> bi.move('a5')
            ('Bc3', 'Ba5', 1478409921.816137)
        """
        old_coor = self.algebraic_to_numeric(self.position)
        new_coor = self.algebraic_to_numeric(position)
        coor_0 = old_coor[0] - new_coor[0]
        coor_1 = old_coor[1] - new_coor[1]
        if coor_0 < 0:
            coor_0 = coor_0 * -1
        if coor_1 < 0:
            coor_1 = coor_1 * -1
        if coor_0 == coor_1:
            return True
        else:
            return False


class King(ChessPiece):
    """A subclass of ChessPiece, for Bishop.

    Attributes:
        prefix (str): Represents the Bishop pieces.
    """
    prefix = 'K'

    def __init__(self, position):
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """Test if the move is legal.

        Args:
            position (str): The algebraic notation of the new position of the
                            piece.

        Returns:
            bool: True, if legal. Else False.

        Examples:
            >>> ki = King('a1')
            >>> ki.prefix
            'K'
            >>> ki.move('a3')
            False
            >>> ki.move('b1')
            ('Ka1', 'Kb1', 1478411970.478926)
            >>> ki.move('a2')
            ('Kb1', 'Ka2', 1478411976.243246)
            >>> ki.move('h3')
            False
        """
        old_coor = self.algebraic_to_numeric(self.position)
        new_coor = self.algebraic_to_numeric(position)
        coor_0 = old_coor[0] - new_coor[0]
        coor_1 = old_coor[1] - new_coor[1]
        if coor_0 < 0:
            coor_0 = coor_0 * -1
        if coor_1 < 0:
            coor_1 = coor_1 * -1
        if (coor_0 == 1 and coor_1 == 0) or (coor_0 == 0 and coor_1 == 1):
            return True
        elif (coor_0 == 0 and coor_1 == 0) or (coor_0 == 1 and coor_1 == 1):
            return True
        else:
            return False


class ChessMatch(ChessPiece):
    """It functions as the gameboard and tracks the moves of the pieces."""

    def __init__(self, pieces=None):
        """Constructor for ChessMatch class.

        Args:
            pieces (dict): a dictionary of pieces keyed by their full notation
                           on the board. Default: None

        Attributes:
            log (list): a list of tuples that stores the history of the game.
        """
        if pieces is None:
            self.reset()
        else:
            self.pieces = pieces

        self.log = []

    def reset(self):
        """A method that resets the match from the beginning."""
        self.log = []
        self.pieces = {
            'Ra1': Rook,
            'Rh1': Rook,
            'Ra8': Rook,
            'Rh8': Rook,
            'Bc1': Bishop,
            'Bf1': Bishop,
            'Bc8': Bishop,
            'Bf8': Bishop,
            'Ke1': King,
            'Ke8': King
        }

    def move(self, piece, position):
        """A function that moves the chess piece and record it to the log.

        Args:
            piece (str): the name of the piece in Full Notation
            position (str): the destination coordinate in short notation.

        Returns:
            tuple: A tuple that includes the old position, the new position,
                   and the timestamp of the move. If the move is not legal,
                   returns False.

        Examples:
            >>> ro_1 = Rook('a1')
            >>> ro_2 = Rook('b1')
            >>> match = ChessMatch({'Ra1': ro_1, 'Rb1': ro_2})
            >>> match.move('Ra1', 'a2')
            >>> match.log
            [('Ra1', 'Ra2', 1478485600.598924)]
            >>> match.move('Rb1', 'c1')
            >>> match.log
            [('Ra1', 'Ra2', 1478485600.598924), ('Rb1', 'Rc1',
            1478485633.515734)]
            >>> match.move('Rc1', 'f4')
            False
        """

        def pi_move(self):
            """A method that moves the piece if the position is allowed."""
            piece1.move(position)
            if not piece1.moves:
                print False
                return
            self.log.append(piece1.moves[0])
            self.pieces[piece[0]+position] = self.pieces.pop(piece)

        if piece[0] == 'R':
            piece1 = Rook(str(piece[-2:]))
            pi_move(self)

        elif piece[0] == 'B':
            piece1 = Bishop(str(piece[-2:]))
            pi_move(self)

        elif piece[0] == 'K':
            piece1 = King(str(piece[-2:]))
            pi_move(self)

    def __len__(self):
        """A magic method that returns the number of log items."""
        return len(self.log)
