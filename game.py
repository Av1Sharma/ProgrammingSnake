import random

# Directions
UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction

    def take_step(self, position, grow=False):
        if grow:
            self.body = self.body + [position]
        else:
            self.body = self.body[1:] + [position]

    def set_direction(self, direction):
        self.direction = direction

    def head(self):
        return self.body[-1]


class Apple:
    def __init__(self, position):
        self.position = position


class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.score = 0
        self.snake = Snake([(0, 0), (1, 0), (2, 0), (3, 0)], RIGHT)
        self.apple = None
        self.generate_apple()

    def generate_apple(self):
        # Generate an apple in a random spot not occupied by the snake
        snake_coords = set(self.snake.body)
        available_cells = [
            (x, y)
            for x in range(self.width)
            for y in range(self.height)
            if (x, y) not in snake_coords
        ]
        if available_cells:
            self.apple = Apple(random.choice(available_cells))
        else:
            self.apple = None  # Board completely filled (win condition!)

    def board_matrix(self):
        matrix = [[None for _ in range(self.width)] for _ in range(self.height)]

        # Place apple
        if self.apple:
            ax, ay = self.apple.position
            a_row = self.height - 1 - ay
            a_col = ax
            if 0 <= a_row < self.height and 0 <= a_col < self.width:
                matrix[a_row][a_col] = "*"

        # Place snake body
        for x, y in self.snake.body:
            row = self.height - 1 - y
            col = x
            if 0 <= row < self.height and 0 <= col < self.width:
                matrix[row][col] = "O"

        # Place snake head
        hx, hy = self.snake.head()
        h_row = self.height - 1 - hy
        h_col = hx
        if 0 <= h_row < self.height and 0 <= h_col < self.width:
            matrix[h_row][h_col] = "X"

        return matrix

    def render(self):
        matrix = self.board_matrix()

        print(f"Score: {self.score}")
        print("+" + "-" * self.width + "+")
        for row in matrix:
            row_str = "".join(" " if cell is None else str(cell) for cell in row)
            print(f"|{row_str}|")
        print("+" + "-" * self.width + "+")

    def next_head(self):
        hx, hy = self.snake.head()
        dx, dy = self.snake.direction
        return (hx + dx, hy + dy)

    def step(self):
        new_head = self.next_head()

        # Wall collision check
        x, y = new_head
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False

        eating = self.apple and new_head == self.apple.position

        # Self collision check: if eating, tail stays; if not, tail moves forward
        body_to_check = self.snake.body if eating else self.snake.body[1:]
        if new_head in body_to_check:
            return False

        if eating:
            self.score += 1
            self.snake.take_step(new_head, grow=True)
            self.generate_apple()
        else:
            self.snake.take_step(new_head, grow=False)

        return True

    def play(self):
        controls = {
            "w": UP,
            "s": DOWN,
            "a": LEFT,
            "d": RIGHT,
        }

        opposites = {
            UP: DOWN,
            DOWN: UP,
            LEFT: RIGHT,
            RIGHT: LEFT,
        }

        while True:
            self.render()
            try:
                cmd = input("Direction [w/a/s/d or Enter to continue, q to quit]: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\nExiting game.")
                break

            if cmd == "q":
                print(f"Thanks for playing! Final Score: {self.score}")
                break

            if cmd in controls:
                desired_dir = controls[cmd]
                if desired_dir != opposites[self.snake.direction]:
                    self.snake.set_direction(desired_dir)

            alive = self.step()
            if not alive:
                self.render()
                print(f"\n💥 CRASH! Game Over. Final Score: {self.score}")
                break


if __name__ == "__main__":
    game = Game(10, 20)
    game.play()