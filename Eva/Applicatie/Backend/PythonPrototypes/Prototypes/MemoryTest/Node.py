class Node(object):
    key = None


    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.val = 0
        self.height = 1
