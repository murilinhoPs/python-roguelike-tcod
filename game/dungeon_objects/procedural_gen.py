from game.dungeon_objects.rooms import RectangularRoom
from game.map_objects import tile_types
from game.map_objects.game_map import GameMap


def generate_dungeon(map_width, map_height) -> GameMap:
    dungeon = GameMap(map_width, map_height)

    room_1 = RectangularRoom(x=20, y=15, width=13, height=15)
    room_2 = RectangularRoom(x=35, y=15, width=10, height=15)

    dungeon.tiles[room_1.inner_area] = tile_types.floor
    print("inner_area_1 X should be: 21 to 33 -> actual: ", room_1.inner_area[0])
    print("inner_area_1 X should be: 16 to 30 -> actual: ", room_1.inner_area[1])
    dungeon.tiles[room_2.inner_area] = tile_types.floor

    return dungeon
