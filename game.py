# Directions
UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction

    def take_step(self, position):
        self.body = self.body[1:] + [position]

    def set_direction(self, direction):
        self.direction = direction

    def head(self):
        return self.body[-1]


class Apple:
    pass


class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.snake = Snake([(0, 0), (1, 0), (2, 0), (3, 0)], RIGHT)

    def board_matrix(self):
        matrix = [[None for _ in range(self.width)] for _ in range(self.height)]

        for x, y in self.snake.body:
            row = self.height - 1 - y
            col = x
            if 0 <= row < self.height and 0 <= col < self.width:
                matrix[row][col] = "O"

        hx, hy = self.snake.head()
        h_row = self.height - 1 - hy
        h_col = hx
        if 0 <= h_row < self.height and 0 <= h_col < self.width:
            matrix[h_row][h_col] = "X"

        return matrix

    def render(self):
        matrix = self.board_matrix()

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
        self.snake.take_step(new_head)

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
                print("Thanks for playing!")
                break

            if cmd in controls:
                desired_dir = controls[cmd]
                if desired_dir != opposites[self.snake.direction]:
                    self.snake.set_direction(desired_dir)

            self.step()


if __name__ == "__main__":
    game = Game(10, 20)
    game.play()