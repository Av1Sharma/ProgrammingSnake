class Snake:
    pass


class Apple:
    pass


class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def board_matrix(self):
        # A 2D list of dimensions (height x width) with None in every square
        return [[None for _ in range(self.width)] for _ in range(self.height)]

    def render(self):
        matrix = self.board_matrix()

        # Top border
        print("+" + "-" * self.width + "+")

        # Each row with side borders
        for row in matrix:
            row_str = "".join(" " if cell is None else str(cell) for cell in row)
            print(f"|{row_str}|")

        # Bottom border
        print("+" + "-" * self.width + "+")


if __name__ == "__main__":
    game = Game(10, 20)
    game.render()