class QueueFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def remove(self):
        if self.is_empty():
            raise Exception("Empty frontier!")
        return self.frontier.pop(0)

    def is_empty(self):
        return len(self.frontier) == 0


class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def remove(self):
        if self.is_empty():
            raise Exception("Empty frontier!")
        return self.frontier.pop()

    def is_empty(self):
        return len(self.frontier) == 0
