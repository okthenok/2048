import numpy
import random
import pygame

class Grid:
    def __init__(self):
        self.board = numpy.zeros((4, 4))

    def render_grid(self, window):
        for x in range(4):
            for y in range(4):
                rect = pygame.Rect(x*20, y*20, 20, 20)
                pygame.draw.rect(window, pygame.Color(245, 245, 245, 1), rect)


# randomly select blocks until we find an empty one
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

# instead of checking everything, check column/row if a block was moved
    def move(self, direction):
        merged = False
        # scan in the opposite direction of movement
        if direction == "up":
            for x in range(4, -1, -1):
                for y in range(4, -1, -1):
                    temp_x, temp_y = x, y
                    while self.block_can_move_in_direction([temp_x, temp_y], "up") and merged is False:
                        if self.merge([temp_x, temp_y], [temp_x, temp_y - 1]):
                            merged = True
                        else:
                            self.board[temp_x, temp_y - 1] = self.board[temp_x, temp_y]
                        temp_y -= 1
                    merged = False
        if direction == "down":
            for x in range(4, -1, -1):
                for y in range(0, 5):
                    temp_x, temp_y = x, y
                    while self.block_can_move_in_direction([temp_x, temp_y], "down") and merged is False:
                        if self.merge([temp_x, temp_y], [temp_x, temp_y + 1]):
                            merged = True
                        else:
                            self.board[temp_x, temp_y + 1] = self.board[temp_x, temp_y]
                        temp_y += 1
                    merged = False
        if direction == "left":
            for x in range(0, 5):
                for y in range(4, -1, -1):
                    temp_x, temp_y = x, y
                    while self.block_can_move_in_direction([temp_x, temp_y], "left") and merged is False:
                        if self.merge([temp_x - 1, temp_y]):
                            merged = True
                        else:
                            self.board[temp_x - 1, temp_y] = self.board[temp_x, temp_y]
                        temp_x -= 1
        if direction == "right":
            for x in range(4, -1, -1):
                for y in range(4, -1, -1):
                    temp_x, temp_y = x, y
                    while self.block_can_move_in_direction([temp_x, temp_y], "right") and merged is False:
                        if self.merge([temp_x, temp_y], [temp_x + 1, temp_y]):
                            merged = True
                        else:
                            self.board[temp_x + 1, temp_y] = self.board[temp_x, temp_y]
                        temp_x += 1
                    merged = False

    def merge(self, block1_pos, block2_pos):
        if self.board[block1_pos] != 0 and self.board[block1_pos] == self.board[block2_pos]:
            self.board[block2_pos] = self.board[block2_pos] * 2
            self.board[block1_pos] = 0
            return True
        else:
            return False

    def block_can_move_in_direction(self, block_position, direction):
        if self.board[block_position] == 0:
            return False
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
    # def search_blocks(self):
    #    blocks = []
    #    xPos, yPos = 0, 0
    #    # (0, 0) is the top left corner
    #    for x in range(4):
    #        for y in range(4):
    #            if(self.board[x, y] != 0):
    #                blocks.append([x, y])
    #    return blocks

