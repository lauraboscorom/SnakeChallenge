"""
    Created on Tue Jun 21 10:27:15 2022
    @author: Laura Bosco Romero
"""

import copy
import numpy as np

class Board:
    """ Board class definition """
  
    def __init__(self, array):
        self.array = array
        self.columns = array[0]
        self.rows = array[1]
    
    # GETTERS
    @property
    def array(self):
        """ Getter for array """
        return self._array
    
    @property
    def columns(self):
        """ Getter for columns """
        return self._columns
    
    @property
    def rows(self):
        """ Getter for rows """
        return self._rows

    # SETTERS
    @array.setter
    def array(self, value):
        """ Setter for array """
        if len(value) != 2:
            raise ValueError("Board length must be 2")
        self._array = value

    @columns.setter
    def columns(self, value):
        """ Setter for columns """
        if value < 1 or \
           value > 10:
            raise ValueError("Board columns exceeds length limits (0-10)")
        self._columns = value

    @rows.setter
    def rows(self, value):
        """ Setter for rows """
        if value < 1 or \
           value > 10:
            raise ValueError("Board rows exceeds length limits (0-10)")
        self._rows = value
        
class Snake:
    """ Snake class definition """
  
    def __init__(self, body):
        self.body = body
    
    # GETTERS
    @property
    def body(self):
        """ Getter for body """
        return self._body

    # SETTERS
    @body.setter
    def body(self, value):
        """ Setter for body """
        if len(value) < 3 or \
           len(value) > 7:
               raise ValueError("Snake's body exceeds its limits (3-7)")
        
        if not all(len(l) == 2 for l in value):
            raise ValueError("Snake's body positions length must be 2")
        
        if not all(l[0] >= 0 for l in value) or \
           not all(l[1] >= 0 for l in value):
               raise ValueError("Snake's body positions are less than 0")
        
        if not all(l != value[0] for l in value[1:]):
            raise ValueError("Snake is self-intersecting")
        
        self._body = value
        
class Path:
    """ Path class definition """
  
    def __init__(self, steps):
        self.steps = steps
    
    def __str__(self):
        return "".join(map(str, self.steps))
    
    def __repr__(self):
        return self.__str__()
    
    # GETTERS    
    @property
    def steps(self):
        """ Getter for steps """
        return self._steps

    # SETTERS    
    @steps.setter
    def steps(self, value):
        """ Setter for steps """
        self._steps = value
    
    def addStep(self, direction):
        self.steps.append(direction)
        
class Game:
    """ Game class definition """

    def __init__(self, board, snake: Snake, depth):
        self.board = board
        self.snake = snake
        self.depth = depth
    
    # GETTERS
    @property
    def board(self):
        """ Getter for board """
        return self._board
    
    @property
    def snake(self):
        """ Getter for snake """
        return self._snake
    
    @property
    def depth(self):
        """ Getter for depth """
        return self._depth

    # SETTERS
    @board.setter
    def board(self, value):
        """ Setter for board """
        self._board = value
    
    @snake.setter
    def snake(self, value):
        """ Setter for snake """
        if not all(l[0] < self.board.columns for l in value.body) or \
           not all(l[1] < self.board.rows for l in value.body):
               raise ValueError("Snake's body positions exceeds board's length")
        self._snake = value
    
    @depth.setter
    def depth(self, value):
        """ Setter for depth """
        if value < 1 or \
           value > 20:
               raise ValueError("Depth exceeds length limits (0-20)")
        self._depth = value
    
    def getAvailableMovements(self, path = None):
        directions = {'U': [0,-1], 'R': [1,0], 'D': [0,1], 'L': [-1,0]}
        availableMovements = []
        head = self.snake.body[0]
        
        for dirStr, dirPath in directions.items():
            headPosition = np.array(head) + dirPath
            try:
                snakePosition = self.snake.body[:-1]
                snakePosition.insert(0, headPosition.tolist())

                # Checking constraints
                snake = Snake(snakePosition)
                game = Game(self.board, snake, self.depth)
                
                if path == None:
                    tempPath = Path([dirStr])
                else:
                    tempPath = Path(copy.deepcopy(path.steps))
                    tempPath.addStep(dirStr)
                
                if self.depth > len(tempPath.steps):
                    for elem in game.getAvailableMovements(tempPath):
                        availableMovements.append(elem)
                else:
                    availableMovements.append(tempPath)
                
            except ValueError:
                pass
        return availableMovements


def numberOfAvailableDifferentPaths(board, snake, depth):
    boardObj = Board(board)
    snakeObj = Snake(snake)
    game = Game(boardObj, snakeObj, depth)
    
    return len(game.getAvailableMovements())