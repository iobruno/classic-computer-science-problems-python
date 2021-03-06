from constraint_satisfaction_problems.csp import Constraint, V, D
from typing import Dict


class ZookeeperConstraint:

    class Rejects(Constraint[str, str]):
        def __init__(self, animal: str, neighbor_animal: str, reason: str = None):
            super().__init__([animal, neighbor_animal])
            self.animal1: str = animal
            self.animal2: str = neighbor_animal
            self.reason: str = reason

        def is_satisfied_with(self, assignment: Dict[str, int]) -> bool:
            if self.animal1 not in assignment or self.animal2 not in assignment:
                return True

            return assignment[self.animal1] != assignment[self.animal2]

    class MustBeTogetherWith(Constraint[str, str]):
        def __init__(self, animal: str, neighbor_animal: str, reason: str = None):
            super().__init__([animal, neighbor_animal])
            self.animal1: str = animal
            self.animal2: str = neighbor_animal
            self.reason: str = reason

        def is_satisfied_with(self, assignment: Dict[str, str]) -> bool:
            """
            Assignment carries the whole configuration of which animals are assigned to which cage
            Meaning: if animal2 IS NOT in it, the assignment is free for animal1 to use, and vice-versa

            Otherwise, if both are in it, the constraint is satisfied:
            AS LONG AS animal1 and animal2 are BOTH in the SAME cage
            """
            if self.animal1 not in assignment or self.animal2 not in assignment:
                return True

            return assignment[self.animal1] == assignment[self.animal2]

    class MustBeInCageID(Constraint[str, int]):
        def __init__(self, animal: str, cage: int, reason: str = None):
            super().__init__([animal])
            self.animal: str = animal
            self.cage_number: int = cage
            self.reason: str = reason

        def is_satisfied_with(self, assignment: Dict[str, int]) -> bool:
            """
            Assignment carries the whole configuration of which animals are assigned to which cage
            Meaning: self.animal must have been assigned to specific self.cage
            for this Constraint to be accepted, otherwise Reject
            """
            return assignment[self.animal] == self.cage_number

    class RejectsSameOrAdjacent(Constraint[str, str]):
        def __init__(self, animal: str, another_animal: str, reason: str = None):
            super().__init__([animal, another_animal])
            self.animal1 = animal
            self.animal2 = another_animal
            self.reason: str = reason

        def is_satisfied_with(self, assignment: Dict[str, int]) -> bool:
            """
            Assignment carries the whole configuration of which animals are assigned to which cage
            Meaning: if animal2 IS NOT in it, the assignment is free for animal1 to use, and vice-versa

            Otherwise, if both are in it, the constraint is satisfied:
            AS LONG AS animal1 and animal2 are NOT in the same or adjacent cages
            """

            if self.animal1 not in assignment or self.animal2 not in assignment:
                return True

            animal1_cage: int = assignment[self.animal1]
            animal2_cage: int = assignment[self.animal2]

            if animal1_cage == animal2_cage:
                return False

            return abs(animal1_cage - animal2_cage) > 1
