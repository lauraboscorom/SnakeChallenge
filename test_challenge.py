"""
    Created on Tue Jun 22 13:43:28 2022
    @author: Laura Bosco Romero
"""

import unittest
from challenge import numberOfAvailableDifferentPaths

class Testing(unittest.TestCase):
    def test1(self):
        board = [4, 3]
        snake = [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
        depth = 3
        result = 7

        self.assertEqual(numberOfAvailableDifferentPaths(board, snake, depth), result)
    
    def test2(self):
        board = [2, 3]
        snake = [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
        depth = 10
        result = 1

        self.assertEqual(numberOfAvailableDifferentPaths(board, snake, depth), result)
    
    def test3(self):
        board = [10, 10]
        snake = [[5,5], [5,4], [4,4], [4,5]]
        depth = 4
        result = 81

        self.assertEqual(numberOfAvailableDifferentPaths(board, snake, depth), result)

if __name__ == '__main__':
    unittest.main()