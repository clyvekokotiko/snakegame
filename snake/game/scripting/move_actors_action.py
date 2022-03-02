from game.scripting.action import Action
from game.casting.cast import Cast


# TODO: Implement MoveActorsAction class here! 

# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor

class MoveActorsAction(Action):
    """
    This class is one thats shows knowledge of polymophism as this class has a function that overides one
    thats written previously.

    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.

    Args:
            class Action: Inherits all attributes form the class called action

    """
    cast = Cast

    def __init__(self) -> None:
        pass

    def execute(self, cast, script):
        """Executes something that is important in the game. This method should be overriden by 
        derived classes.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        actors = cast.get_all_actors()

        for actor in actors:
            actor.move_next()
