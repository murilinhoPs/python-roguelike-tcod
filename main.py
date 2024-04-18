#!/usr/bin/env python3
from __future__ import annotations

import tcod

from game.actions import MovementAction, EscAction
from game.entity import Entity
from game.input_handlers import EventHandler


def main() -> None:
    screen_width = 80
    screen_height = 50
    tileset = tcod.tileset.load_tilesheet(
        "data/dejavu10_10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    event_handler = EventHandler()
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset,
            title="Yet Another Roguelike Tutorial",
            vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")

        while True:
            root_console.print(x=player.x, y=player.y, string=player.char, fg=player.color)
            root_console.print(x=npc.x, y=npc.y, string=npc.char, fg=npc.color)

            context.present(root_console)
            root_console.clear()

            for event in tcod.event.wait():
                action = event_handler.dispatch(event)
                if action is None:
                    continue
                if isinstance(action, MovementAction):
                    player.move(action.dx, action.dy)
                elif isinstance(action, EscAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()
