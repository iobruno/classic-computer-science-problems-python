import pytest
from constraint_satisfaction_problems.csp import CSP
from constraint_satisfaction_problems.zookeeper import ZookeeperConstraint
from typing import Dict, Optional


class TestZookeeperConstraintProblem:

    def test_valid_zoo_configuration(self, zoo_organization_problem):
        result: Optional[Dict[str, int]] = zoo_organization_problem

        assert result['Lion'] == 1
        assert result['Meerkat'] == 1
        assert result['Wild Boar'] == 1
        assert result['Tiger'] == 2
        assert result['Peacock'] == 3
        assert result['Deer'] == 4


@pytest.fixture
def zoo_organization_problem() -> Optional[Dict[str, int]]:
    domain = [1, 2, 3, 4]
    problem = CSP() \
        .add_variable(var="Lion", domain=domain) \
        .add_variable(var="Deer", domain=domain) \
        .add_variable(var="Hyena", domain=domain) \
        .add_variable(var="Tiger", domain=domain) \
        .add_variable(var="Peacock", domain=domain) \
        .add_variable(var="Meerkat", domain=domain) \
        .add_variable(var="Wild Boar", domain=domain)

    problem \
        .add_constraint(ZookeeperConstraint.Reject("Lion", "Tiger")) \
        .add_constraint(ZookeeperConstraint.MustBeTogetherWith("Meerkat", "Wild Boar")) \
        .add_constraint(ZookeeperConstraint.Reject("Hyena", "Lion")) \
        .add_constraint(ZookeeperConstraint.Reject("Hyena", "Deer")) \
        .add_constraint(ZookeeperConstraint.Reject("Hyena", "Peacock")) \
        .add_constraint(ZookeeperConstraint.Reject("Hyena", "Meerkat")) \
        .add_constraint(ZookeeperConstraint.Reject("Hyena", "Wild Boar")) \
        .add_constraint(ZookeeperConstraint.Reject("Tiger", "Meerkat")) \
        .add_constraint(ZookeeperConstraint.Reject("Tiger", "Wild Boar")) \
        .add_constraint(ZookeeperConstraint.Reject("Tiger", "Peacock")) \
        .add_constraint(ZookeeperConstraint.Reject("Deer", "Lion")) \
        .add_constraint(ZookeeperConstraint.Reject("Deer", "Tiger")) \
        .add_constraint(ZookeeperConstraint.MustNotBeInAdjacentCageWith("Deer", "Lion")) \
        .add_constraint(ZookeeperConstraint.MustNotBeInAdjacentCageWith("Deer", "Tiger")) \
        .add_constraint(ZookeeperConstraint.Reject("Peacock", "Lion")) \
        .add_constraint(ZookeeperConstraint.MustBeInCageID("Lion", 1))

    return problem.backtracking_search()
