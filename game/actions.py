class Action:
    pass


class EscAction(Action):
    pass


class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        # super().__init__()

        self.dx = dx
        self.dy = dy