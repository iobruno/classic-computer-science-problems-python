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
