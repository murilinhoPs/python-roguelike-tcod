from typing import Set, Iterable, Any

from tcod.console import Console
from tcod.context import Context

from game.actions import MovementAction, EscAction
from game.entity import Entity
from game.input_handlers import EventHandler
from game.map_objects.game_map import GameMap


class Engine:
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, game_map: GameMap, player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player

    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue
            if isinstance(action, MovementAction):
                if self.game_map.tiles["walkable"][self.player.x + action.dx, self.player.y + action.dy]:
                    # if the "walkable" position that player is going (current_pos -> designed_pos) is walkable (true)
                    # tiles["walkable"] -> prints ONLY the walkable property from tile
                    # tiles["walkable"][1, 2] -> prints ONLY the walkable property from row 1, column 2
                    self.player.move(dx=action.dx, dy=action.dy)
            elif isinstance(action, EscAction):
                raise SystemExit()

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)
        for entity in self.entities:
            console.print(x=entity.x, y=entity.y, string=entity.char, fg=entity.color)

        context.present(console)
        console.clear()
