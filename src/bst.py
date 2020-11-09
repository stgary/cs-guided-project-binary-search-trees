class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # duplicates go on the right 
    def insert(self, value):
        # base case(s)
        # we realize we need to go in a direction, but 
        # there's no node in said direction, so we can 
        # put the value in this spot 

        # how we get closer to a base case?
        # after determining the direction we need to go in,
        # we see that there's a node in that spot, so we go there 
        if value < self.value:
            # go left 
            if self.left is None:
                self.left = BSTNode(value)
            else:
                # move left down the tree 
                self.left.insert(value)
        # duplicates go on to the right 
        else:
            # go right 
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # move right down the tree 
                self.right.insert(value)

    # Asking a question, expects an answer 
    def search(self, target):
        # base case(s)
        # 1. We found what we were looking for 
        if self.value == target:
            return self
        # go left 
        elif target < self.value:
            # 2. We've looked through where the element must be 
            # if it existed in the tree, but we didn't find it 
            if self.left is None:
                return False
            else:
                # we need to go left, do so by calling the left
                # child's `search` method 
                return self.left.search(target)
        # go right 
        else:
            if self.right is None:
                return False
            else:
                # we need to go right, do so by calling the right
                # child's `search` method 
                return self.right.search(target)
				