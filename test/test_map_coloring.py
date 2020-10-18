import pytest
from constraint_satisfaction_problems.csp import CSP
from constraint_satisfaction_problems.map_coloring import MapColoringConstraint


class TestAustralianMapColoringProblem:

    def test_western_australia_does_not_collide_with_neighbors(self, australian_map_coloring_problem):
        result = australian_map_coloring_problem
        assert result['Western Australia'] not in [
            result['Northern Territory'],
            result['South Australia']
        ]

    def test_northern_territory_does_not_collide_with_neighbors(self, australian_map_coloring_problem):
        result = australian_map_coloring_problem
        assert result['Northern Territory'] not in [
            result['Western Australia'],
            result['South Australia'],
            result['Queensland'],
        ]

    def test_south_australia_does_not_collide_with_neighbors(self, australian_map_coloring_problem):
        result = australian_map_coloring_problem
        assert result['South Australia'] not in [
            result['Western Australia'],
            result['Northern Territory'],
            result['Queensland'],
            result['New South Wales'],
            result['Victoria']
        ]

    def test_queensland_does_not_collide_with_neighbors(self, australian_map_coloring_problem):
        result = australian_map_coloring_problem
        assert result['Queensland'] not in [
            result['Northern Territory'],
            result['South Australia'],
            result['New South Wales']
        ]

    def test_new_south_wales_does_not_collide_with_neighbors(self, australian_map_coloring_problem):
        result = australian_map_coloring_problem
        assert result['New South Wales'] not in [
            result['Queensland'],
            result['South Australia'],
            result['Victoria']
        ]

    def test_victoria_does_not_collide_with_neighbors(self, australian_map_coloring_problem):
        result = australian_map_coloring_problem
        assert result['Victoria'] not in [
            result['South Australia'],
            result['New South Wales'],
            result['Tasmania']
        ]

    def test_tasmania_does_not_collide_with_neighbors(self, australian_map_coloring_problem):
        result = australian_map_coloring_problem
        assert result['Tasmania'] not in [
            result['Victoria']
        ]


@pytest.fixture
def australian_map_coloring_problem():
    domain = ["red", "green", "blue"]
    csp = CSP().add_variable(var="Western Australia", domain=domain) \
        .add_variable(var="Northern Territory", domain=domain) \
        .add_variable(var="South Australia", domain=domain) \
        .add_variable(var="Queensland", domain=domain) \
        .add_variable(var="New South Wales", domain=domain) \
        .add_variable(var="Victoria", domain=domain) \
        .add_variable(var="Tasmania", domain=domain)

    csp.add_constraint(MapColoringConstraint("Western Australia", "Northern Territory")) \
        .add_constraint(MapColoringConstraint("Western Australia", "South Australia")) \
        .add_constraint(MapColoringConstraint("South Australia", "Northern Territory")) \
        .add_constraint(MapColoringConstraint("Queensland", "Northern Territory")) \
        .add_constraint(MapColoringConstraint("Queensland", "South Australia")) \
        .add_constraint(MapColoringConstraint("Queensland", "New South Wales")) \
        .add_constraint(MapColoringConstraint("New South Wales", "South Australia")) \
        .add_constraint(MapColoringConstraint("Victoria", "South Australia")) \
        .add_constraint(MapColoringConstraint("Victoria", "New South Wales")) \
        .add_constraint(MapColoringConstraint("Victoria", "Tasmania"))

    return csp.backtracking_search()
