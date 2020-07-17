class BSTNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        if value > self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        pass

    def contains(self, target):
        if self.value == target:
            return True
        does_contain = False
        if self.value >= target:
            if self.left is None:
                return False
            does_contain = self.left.contains(target)
        if self.value < target:
            if self.right is None:
                return False
            does_contain = self.right.contains(target)
        return does_contain
        pass