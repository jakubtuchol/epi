from src.graphs import BLACK
from src.graphs import fill_surrounded_regions
from src.graphs import flip_color
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
