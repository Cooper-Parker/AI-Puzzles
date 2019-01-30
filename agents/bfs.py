# Breadth-First Search Agent

from solving.utils.framework import Agent
from solving.utils.structures import Queue, SearchTree

class BFSAgent(Agent):

    def __init__(self):
        self.moves = dict()

    # Return the move this agent wants to make
    def move(self, puzzle):

        # Plan a move if necessary
        if puzzle not in self.moves:
            self.bfs(puzzle)

        return self.moves[puzzle]

    # Use breadth-first search to plan moves
    def bfs(self, puzzle):

        tree = SearchTree(puzzle)

        frontier = Queue()
        frontier.push(puzzle)

        while len(frontier) > 0:
            # remove the oldest thing from the queue
            leaf = frontier.pop()

            # look through the list of moves 1 by 1
            for move in leaf.moves():
                neighbor = leaf.neighbor(move)

                if neighbor not in tree:
                    tree.connect(neighbor, leaf, move)
                    frontier.push(neighbor)

                    if neighbor.solved():
                        self.moves = tree.branch(neighbor)
                        return

        print("Failed :(")
        quit()