import pytest

from src.graphs import BLACK
from src.graphs import fill_surrounded_regions
from src.graphs import flip_color
from src.graphs import get_neighbors
from src.graphs import WHITE


@pytest.fixture(scope='module')
def create_maze():
    """
    Create 2d maze
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
    return maze


class TestGetNeighbors(object):
    """
    Testing get_neighbors method
    """

    def test_get_all_neighbors(self, create_maze):
        neighbors = get_neighbors((8, 5), create_maze)
        assert 4 == len(neighbors)
        assert (8, 4) in neighbors
        assert (8, 6) in neighbors
        assert (7, 5) in neighbors
        assert (9, 5) in neighbors

    def test_get_one_neighbor(self, create_maze):
        neighbors = get_neighbors((3, 2), create_maze)
        assert 1 == len(neighbors)
        assert (3, 1) in neighbors

    def test_get_no_neighbors(self, create_maze):
        neighbors = get_neighbors((9, 9), create_maze)
        assert 0 == len(neighbors)

    """
class TestSearchMaze(object):
    Question 19.1
    def test_book_example(self, create_maze):
        start_coord = (9,0)
        end_coord = (0,9)
        path = search_maze(create_maze, start_coord, end_coord)
        assert path[0] == start_coord
        assert path[-1] == end_coord
    """


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
