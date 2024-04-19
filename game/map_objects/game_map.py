import numpy as np
from tcod.console import Console

import game.map_objects.tile_types as tile_types


class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full(shape=(width, height), fill_value=tile_types.floor, order="F")

        self.tiles[30:33, 22] = tile_types.wall  # tiles from column (height) 22, from 30 to 33 row (width) is wall

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:  # void
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]  # This method proves much faster than
        # using the console.print method that we use for the individual entities

# Shape is the dimensions of the array. This is a tuple of integers indicating the size of the array in each
# dimension. For a matrix with n rows and m columns, shape will be (n,m). The length of the shape tuple is therefore
# the number of axes, ndim.
