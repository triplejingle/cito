class VariableNode(object):

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.height = 1
        self.value = []
