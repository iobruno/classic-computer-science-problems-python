from constraint_satisfaction_problems.csp import Constraint
from typing import Dict


class MapColoringConstraint(Constraint[str, str]):

    def __init__(self, place1: str, place2: str) -> None:
        super().__init__([place1, place2])
        self.place1: str = place1
        self.place2: str = place2

    def is_satisfied_with(self, assignment: Dict[str, str]) -> bool:
        """
        If either place is not in the assignment, then it is not
        yet possible for their colors to be conflicting

        Otherwise, check the color assigned to place1 is not the same as the
        color assigned to place2
        """
        if self.place1 not in assignment or self.place2 not in assignment:
            return True

        return assignment[self.place1] != assignment[self.place2]
