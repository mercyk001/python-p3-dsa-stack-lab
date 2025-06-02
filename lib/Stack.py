class Stack:
    def __init__(self, items=None, limit=100):
        self.items = list(items) if items else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        # silently ignore if full (based on your test logic)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        '''
        Return the number of pops to get to target from the top.
        Top element is 0 pops away. If not found, return -1.
        '''
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                return len(self.items) - 1 - i
        return -1
