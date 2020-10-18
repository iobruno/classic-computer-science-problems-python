from constraint_satisfaction_problems.csp import Constraint, V, D
from typing import Dict


class ZookeeperConstraint:

    class Reject(Constraint[str, str]):
        def __init__(self, animal, neighbor_animal):
            super().__init__([animal, neighbor_animal])
            self.animal1: str = animal
            self.animal2: str = neighbor_animal

        def is_satisfied_with(self, assignment: Dict[str, int]) -> bool:
            """
            Assignment carries the whole configuration of which animals are assigned to which cage
            Meaning: if animal2 IS NOT in it, the assignment is free for animal1 to use, and vice-versa

            Otherwise, if both are in it, the constraint is satisfied:
            AS LONG AS animal1 and animal2 are NOT in the same cage
            """
            if self.animal1 not in assignment or self.animal2 not in assignment:
                return True

            return assignment[self.animal1] != assignment[self.animal2]

    class MustBeTogether(Constraint[str, str]):
        def __init__(self, animal, neighbor_animal):
            super().__init__([animal, neighbor_animal])
            self.animal1: str = animal
            self.animal2: str = neighbor_animal

        def is_satisfied_with(self, assignment: Dict[str, str]) -> bool:
            pass

    class MustBeInCageID(Constraint[str, int]):
        def __init__(self, animal: str, cage: int):
            super().__init__([animal])
            self.animal: str = animal
            self.cage_number: int = cage

        def is_satisfied_with(self, assignment: Dict[str, int]) -> bool:
            pass
