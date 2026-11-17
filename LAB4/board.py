import random

SIZE = 4


class Board:
    def __init__(self):
        self.grid = [[0] * SIZE for _ in range(SIZE)]
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()

    def add_random_tile(self):
        empty = [(r, c) for r in range(SIZE) for c in range(SIZE) if self.grid[r][c] == 0]
        if empty:
            r, c = random.choice(empty)
            self.grid[r][c] = 4 if random.random() < 0.1 else 2

    @staticmethod
    def slide_line(line):
        values = [x for x in line if x]
        result = []
        score_gained = 0
        skip = False
        
        for i in range(len(values)):
            if skip:
                skip = False
                continue
            if i + 1 < len(values) and values[i] == values[i + 1]:
                merged_value = values[i] * 2
                result.append(merged_value)
                score_gained += merged_value
                skip = True
            else:
                result.append(values[i])
                
        return result + [0] * (SIZE - len(result)), score_gained

    def move_left(self):
        changed = False
        for r in range(SIZE):
            old = self.grid[r][:]
            new_line, points = self.slide_line(old)
            self.grid[r] = new_line
            self.score += points
            changed |= old != self.grid[r]
        return changed

    def move_right(self):
        changed = False
        for r in range(SIZE):
            old = self.grid[r][:]
            new_line, points = self.slide_line(list(reversed(old)))
            self.grid[r] = list(reversed(new_line))
            self.score += points
            changed |= old != self.grid[r]
        return changed

    def move_up(self):
        changed = False
        for c in range(SIZE):
            old = [self.grid[r][c] for r in range(SIZE)]
            new_line, points = self.slide_line(old)
            for r in range(SIZE):
                self.grid[r][c] = new_line[r]
            self.score += points
            changed |= old != new_line
        return changed

    def move_down(self):
        changed = False
        for c in range(SIZE):
            old = [self.grid[r][c] for r in range(SIZE)]
            new_line, points = self.slide_line(list(reversed(old)))
            reversed_new = list(reversed(new_line))
            for r in range(SIZE):
                self.grid[r][c] = reversed_new[r]
            self.score += points
            changed |= old != reversed_new
        return changed

    def can_move(self):
        if any(0 in row for row in self.grid):
            return True
        for r in range(SIZE):
            for c in range(SIZE):
                if c + 1 < SIZE and self.grid[r][c] == self.grid[r][c + 1]:
                    return True
                if r + 1 < SIZE and self.grid[r][c] == self.grid[r + 1][c]:
                    return True
        return False