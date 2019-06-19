import numpy
import random
import pygame

class Grid:
    def __init__(self):
        self.board = numpy.zeros((4, 4))

    def spawn_block(self):
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        if self.board[x, y] == 0:
            if random.random() > 0.9:
                self.board[x, y] = 4
            else:
                self.board[x, y] = 2
            print("Coordinates of spawned block: " + str([x, y]))
            print("Value of spawned block: " + str(self.board[x, y]))
        else:
            spawn_block(self)

    def move(self, direction):
        blocks = self.search_blocks()
        # scan in the opposite direction of movement



    def block_can_move_in_direction(self, block_position, direction):
        if self.board[block_position] == 0:
            return
        else:
            if direction == "up":
                if self.board[block_position[0], block_position[1] - 1] != self.board[block_position] \
                        or block_position[1] - 1 < 0:
                    return False
                else:
                    return True
            if direction == "left":
                if self.board[block_position[0] - 1, block_position[1]] != self.board[block_position] \
                        or block_position[0] - 1 < 0:
                    return False
                else:
                    return True
            if direction == "right":
                if self.board[block_position[0] + 1, block_position[1]] != self.board[block_position] \
                        or block_position[0] + 1 > 3:
                    return False
                else:
                    return True
            if direction == "down":
                if self.board[block_position[0], block_position[1] + 1] != self.board[block_position] \
                        or block_position[0] + 1 > 3:
                    return False
                else:
                    return True

    # returns the positions of all blocks
    def search_blocks(self):
        blocks = []
        xPos, yPos = 0, 0
        # (0, 0) is the top left corner
        for x in range(4):
            for y in range(4):
                if(self.board[x, y] != 0):
                    blocks.append([x, y])
        return blocks
