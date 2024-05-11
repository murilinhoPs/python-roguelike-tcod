from typing import Tuple


class Room:
    pass


class RectangularRoom(Room):
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    @property
    def center(self) -> Tuple[int, int]:
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y

    @property
    def inner_area(self) -> Tuple[slice, slice]:
        """Return the inner area of this room as a 2D array index."""
        # https://rogueliketutorials.com/tutorials/tcod/v2/part-3/
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)  # have at least 1 tile wide wall between rooms
