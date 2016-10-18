import pytest

from src.graphs import BLACK
from src.graphs import fill_surrounded_regions
from src.graphs import flip_color
from src.graphs import GraphNode
from src.graphs import is_minimally_connected
from src.graphs import search_maze
from src.graphs import WHITE


class TestSearchMaze(object):
    """
    Question 19.1
    """

    maze = [
        [BLACK, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK, BLACK, WHITE, WHITE],
        [WHITE, WHITE, BLACK, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
        [BLACK, WHITE, BLACK, WHITE, WHITE, BLACK, BLACK, WHITE, BLACK, BLACK],
        [WHITE, WHITE, WHITE, BLACK, BLACK, BLACK, WHITE, WHITE, BLACK, WHITE],
        [WHITE, BLACK, BLACK, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE],
        [WHITE, BLACK, BLACK, WHITE, WHITE, BLACK, WHITE, BLACK, BLACK, WHITE],
        [WHITE, WHITE, WHITE, WHITE, BLACK, WHITE, WHITE, WHITE, WHITE, WHITE],
        [BLACK, WHITE, BLACK, WHITE, BLACK, WHITE, BLACK, WHITE, WHITE, WHITE],
        [BLACK, WHITE, BLACK, BLACK, WHITE, WHITE, WHITE, BLACK, BLACK, BLACK],
        [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK, BLACK, WHITE],
    ]

    def test_book_example(self):
        start_coord = (9, 0)
        end_coord = (0, 9)
        path = search_maze(self.maze, start_coord, end_coord)
        assert path[0] == start_coord
        assert path[-1] == end_coord


class TestFlipColor(object):
    """
    Question 19.2
    """

    matrix_a = [
        [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 0, 1, 1],
        [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    ]

    matrix_b = [
        [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 0, 1, 1],
        [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    ]

    matrix_c = [
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    def test_book_example(self):
        start = (5, 4)
        output = flip_color(self.matrix_a, start)
        assert self.matrix_b == output

    def test_second_iteration(self):
        start = (3, 6)
        output = flip_color(self.matrix_b, start)
        assert self.matrix_c == output


class TestFillSurroundedRegions(object):
    """
    Question 19.3
    """

    matrix_a = [
        ['B', 'B', 'B', 'B'],
        ['W', 'B', 'W', 'B'],
        ['B', 'W', 'W', 'B'],
        ['B', 'B', 'B', 'B'],
    ]

    matrix_b = [
        ['B', 'B', 'B', 'B'],
        ['W', 'B', 'B', 'B'],
        ['B', 'B', 'B', 'B'],
        ['B', 'B', 'B', 'B'],
    ]

    def test_book_example(self):
        assert self.matrix_b == fill_surrounded_regions(self.matrix_a)


@pytest.fixture(scope='module')
def build_straight_line_graph():
    root = GraphNode()
    one = GraphNode()
    two = GraphNode()
    three = GraphNode()
    four = GraphNode()

    root.add_neighbor(one)
    one.add_neighbor(root)

    one.add_neighbor(two)
    two.add_neighbor(one)

    two.add_neighbor(three)
    three.add_neighbor(two)

    three.add_neighbor(four)
    four.add_neighbor(three)

    return root


@pytest.fixture(scope='module')
def build_branching_graph():
    root = GraphNode()
    one = GraphNode()
    two = GraphNode()
    three = GraphNode()
    four = GraphNode()

    root.add_neighbor(one)
    one.add_neighbor(root)

    root.add_neighbor(two)
    two.add_neighbor(root)

    root.add_neighbor(three)
    three.add_neighbor(root)

    root.add_neighbor(four)
    four.add_neighbor(root)

    return root


@pytest.fixture(scope='module')
def build_cycle_graph():
    one = GraphNode()
    two = GraphNode()
    three = GraphNode()
    four = GraphNode()

    one.add_neighbor(two)
    two.add_neighbor(one)

    two.add_neighbor(three)
    three.add_neighbor(two)

    three.add_neighbor(four)
    four.add_neighbor(three)

    four.add_neighbor(one)
    one.add_neighbor(four)

    one.add_neighbor(three)
    three.add_neighbor(one)

    return one


class TestIsMinimallyConnected(object):
    """
    Question 19.4
    """

    def test_straight_line_graph(self, build_straight_line_graph):
        assert is_minimally_connected(build_straight_line_graph)

    def test_none_case(self):
        assert is_minimally_connected(None)

    def test_star_case(self, build_branching_graph):
        assert is_minimally_connected(build_branching_graph)

    def test_cycle_case(self, build_cycle_graph):
        assert not is_minimally_connected(build_cycle_graph)
