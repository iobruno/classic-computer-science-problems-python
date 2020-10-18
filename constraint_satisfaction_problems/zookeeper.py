from constraint_satisfaction_problems.csp import Constraint, V, D
from typing import Dict


class ZookeeperConstraint:

    class Reject(Constraint[str, str]):
        def __init__(self, animal, neighbor_animal):
            super().__init__([animal, neighbor_animal])
            self.animal1: str = animal
            self.animal2: str = neighbor_animal

        def is_satisfied_with(self, assignment: Dict[str, str]) -> bool:
            pass

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
