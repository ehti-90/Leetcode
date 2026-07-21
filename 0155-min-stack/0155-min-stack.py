class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = []   # second stack for storing min val

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_val or val <= self.min_val[-1]: 
        #  only append to second stack if empty or less than top of min_val stack
            self.min_val.append(val)
        

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()

            # remove smallest val from min_val stack if its also removed from main stack
            if val == self.min_val[-1]:
                self.min_val.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_val[-1] # return second stack top

        
