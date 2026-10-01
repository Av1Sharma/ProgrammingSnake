class Snake:
    pass


class Apple:
    pass


class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def render(self):
        print("Height:", self.height)
        print("Width:", self.width)


if __name__ == "__main__":
    game = Game(10, 20)
    game.render()