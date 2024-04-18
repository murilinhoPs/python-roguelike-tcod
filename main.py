#!/usr/bin/env python3
from __future__ import annotations

import tcod

from actions import MovementAction, EscAction
from input_handlers import EventHandler


def main() -> None:  # returns nothing, um void
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)  # the same as width // 2, but only if the divisor is without dot (i.e 2.0)
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet(
        "./dejavu10_10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    with tcod.context.new_terminal(  # Creates the screen in current context, with (com o new terminal criado...)
            screen_width,
            screen_height,
            tileset=tileset,
            title="Yet Another Roguelike Tutorial",
            vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")  # creates our “console” which is what
        # we’ll be drawing to its current order to draw is [y,x], which is unintuitive. order="F" set its order to [x,y]
        while True:  # game loop
            root_console.print(x=player_x, y=player_y, string="@")  # prints on pos 1x1 @

            context.present(root_console)  # Render the console to the window and show it

            root_console.clear()  # clear the previous player position, after movementAction was performed

            for event in tcod.event.wait():  # waits until some event is performed
                action = event_handler.dispatch(event)
                if action is None:
                    continue  # continue on the loop until any action was taken
                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy
                elif isinstance(action, EscAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()
