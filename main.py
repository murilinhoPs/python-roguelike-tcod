#!/usr/bin/env python3
from __future__ import annotations

import tcod

from game.dungeon_objects.procedural_gen import generate_dungeon
from game.engine import Engine
from game.entity import Entity
from game.input_handlers import EventHandler


def main() -> None:
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45
    event_handler = EventHandler()
    tileset = tcod.tileset.load_tilesheet(
        "data/dejavu10_10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    game_map = generate_dungeon(map_width, map_height)
    engine = Engine(entities, event_handler, game_map, player)

    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset,
            title="Yet Another Roguelike Tutorial",
            vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()
            engine.handle_events(events)


if __name__ == "__main__":
    main()
