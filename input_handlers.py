from __future__ import annotations

import tcod.event

from actions import Action, MovementAction, EscAction


class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self,
                event: tcod.event.Quit) -> Action | None:  # the same as Optional[Action]from typing import Optional
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Action | None:
        action: Action | None = None  # define the current action or none if it doesn't exist

        key = event.sym  # which key was pressed
        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action = EscAction()
        # No valid key was pressed
        return action
