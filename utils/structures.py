from collections import deque

# FIFO structure
class Queue(object):

    def __init__(self):
        self.items = deque()

    def __len__(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        # pop() will return from the end, but popleft() will return from the beginning
        return self.items.popleft()


class SearchTree(object):

    def __init__(self, root):
        self.levels = {root: 0}
        self.parents = dict()
        self.moves = dict()

    def __contains__(self, node):
        return node in self.levels

    def depth(self, node):
        return self.levels[node]

    def connect(self, child, parent, move):
        self.levels[child] = self.levels[parent] + 1
        self.parents[child] = parent
        self.moves[child] = move

    def branch(self, node):
        moves = dict()

        while node in self.parents:
            move = self.moves[node]
            parent = self.parents[node]
            moves[parent] = move
            node = parent

        return moves