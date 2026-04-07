class Robot(object):

    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.dir = 0  # 0=East, 1=North, 2=West, 3=South

        self.directions = ["East", "North", "West", "South"]
        self.moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        self.cycle = 2 * (width + height - 2)

    def step(self, num):
        num %= self.cycle
        
        # special case: if num == 0, robot completes full cycle
        if num == 0:
            num = self.cycle

        while num > 0:
            dx, dy = self.moves[self.dir]
            nx = self.x + dx
            ny = self.y + dy

            # check boundary
            if 0 <= nx < self.w and 0 <= ny < self.h:
                self.x = nx
                self.y = ny
                num -= 1
            else:
                # turn counterclockwise
                self.dir = (self.dir + 1) % 4

    def getPos(self):
        return [self.x, self.y]

    def getDir(self):
        return self.directions[self.dir]
