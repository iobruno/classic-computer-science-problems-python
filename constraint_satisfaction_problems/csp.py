from typing import TypeVar, Generic, Dict, List, Optional, Iterable
from abc import ABC, abstractmethod

V = TypeVar("V")
D = TypeVar("D")


class Constraint(Generic[V, D], ABC):
    """
    Abstract Base Class for all constraints
    """
    variables: Iterable[V]

    def __init__(self, variables: Iterable[V]):
        self.variables = variables

    @abstractmethod
    def is_satisfied_with(self, assignment: Dict[V, D]) -> bool:
        pass


class CSP(Generic[V, D]):
    variables: List[V]
    domains: Dict[V, List[D]]
    constraints: Dict[V, List[Constraint[V, D]]]

    def __init__(self):
        self.variables = list()
        self.domains = dict()
        self.constraints = dict()

    def add_variable(self, var: V, domain: List[D]) -> 'CSP':
        self.variables.append(var)
        self.domains[var] = domain
        self.constraints[var] = list()
        return self

    def add_constraint(self, constraint: Constraint[V, D]) -> 'CSP':
        for var in constraint.variables:
            if var not in self.variables:
                raise LookupError(f"Unknown variable {var} specified in constraint")
            self.constraints[var].append(constraint)
        return self

    def is_consistent(self, var: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[var]:
            if not constraint.is_satisfied_with(assignment):
                return False
        return True

    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        if len(assignment) == len(self.variables):
            return assignment

        unassigned_vars: List[V] = [var for var in self.variables if var not in assignment]
        most_constrained_var = max(unassigned_vars, key=lambda var: len(self.constraints[var]))

        for value in self.domains[most_constrained_var]:
            local_assignment = assignment.copy()
            local_assignment[most_constrained_var] = value

            if self.is_consistent(most_constrained_var, local_assignment):
                result = self.backtracking_search(local_assignment)
                if result is not None:
                    return result

        return None
