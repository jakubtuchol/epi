# Const values for maze problem

WHITE = 'WHITE'
BLACK = 'BLACK'


def search_maze(maze, start, end):
    """
    Question 19.1: Given a 2d array of black and white entries representing
    a maze with designated entrance and exit points, find a path from the
    entrance to the exit.
    """
    path = [start]
    visited = []
    for elt in maze:
        row_visit = []
        for _ in elt:
            row_visit.append(False)
        visited.append(row_visit)

    start_row, start_col = start
    visited[start_row][start_col] = True

    while path:
        # if in has_neighbors, then
        # definitely has neighbors
        row, col = path[-1]

        next_pos = get_next_neighbor(row, col, maze, visited)
        if next_pos:
            path.append(next_pos)
            row_next, col_next = next_pos
            visited[row_next][col_next] = True
            if next_pos == end:
                return path
        else:
            path.pop()
    return None


def get_next_neighbor(row, col, maze, visited):
    # below
    if row > 0 \
        and maze[row - 1][col] == WHITE \
            and not visited[row - 1][col]:
        return row - 1, col
    # above
    if row < len(visited) - 1 \
        and maze[row + 1][col] == WHITE \
            and not visited[row + 1][col]:
        return row + 1, col
    # left
    if col > 0 \
        and maze[row][col - 1] == WHITE \
            and not visited[row][col - 1]:
        return row, col - 1
    # right
    if col < len(visited) - 1 \
        and maze[row][col + 1] == WHITE \
            and not visited[row][col + 1]:
        return row, col + 1

    return None


def flip_color(matrix, start):
    """
    Problem 19.2: Given a boolean matrix and a start
    value, flip the color of all cells reachable
    from the start point
    """
    queue = [start]
    row, col = start
    flipped_color = 0 if matrix[row][col] else 1
    # print('flipping color to {}'.format(flipped_color))

    # generating visited matrix so we don't visit same
    # location multiple times
    visited_matrix = []
    for row_elt in matrix:
        visited_row = []
        for _ in row_elt:
            visited_row.append(False)
        visited_matrix.append(visited_row)

    while queue:
        # print('have queue of len {}'.format(queue))
        point = queue.pop(0)
        row, col = point
        visited_matrix[row][col] = True
        queue.extend(get_adjacent(matrix, point, visited_matrix))
        matrix[row][col] = flipped_color
    return matrix


def get_adjacent(matrix, point, visited):
    row, col = point
    color = matrix[row][col]
    adjacent = []
    # get above
    if row > 0 \
        and matrix[row - 1][col] == color \
            and not visited[row - 1][col]:
        adjacent.append((row - 1, col))

    # get below
    if row < len(matrix) - 1 \
        and matrix[row + 1][col] == color \
            and not visited[row + 1][col]:
        adjacent.append((row + 1, col))

    # get left
    if col > 0 \
        and matrix[row][col - 1] == color \
            and not visited[row][col - 1]:
        adjacent.append((row, col - 1))

    # get right
    if col < len(matrix[0]) - 1 \
        and matrix[row][col + 1] == color \
            and not visited[row][col + 1]:
        adjacent.append((row, col + 1))

    return adjacent


def fill_surrounded_regions(board):
    """
    Question 19.3: Write a program that takes A
    and replaces all W's that cannot reach the
    boundary with B's
    """

    visited = []
    for row_visit in board:
        visit_row = []
        for _ in row_visit:
            visit_row.append(False)
        visited.append(visit_row)

    for row, row_elt in enumerate(board):
        for col, elt in enumerate(row_elt):
            if elt == 'W' and not visited[row][col]:
                mark_if_surrounded(row, col, board, visited)

    return board


def mark_if_surrounded(row, col, board, visited):
    """
    Check if can reach exterior
    """
    if row == 0 or row == len(board) - 1:
        return
    if col == 0 or col == len(board[0]) - 1:
        return

    # otherwise, try to burrow our way out
    to_mark = []
    queue = [(row, col)]

    while queue:
        position = queue.pop(0)
        to_mark.append(position)
        row_visit, col_visit = position
        visited[row_visit][col_visit] = True

        # if this has been visited
        # part of value that is connected
        # to border
        # if visited[row_visit][col_visit]:
        #    return
        if row_visit == 0 or row_visit == len(board) - 1:
            return
        if col_visit == 0 or col_visit == len(board[0]) - 1:
            return
        queue.extend(get_adjacent_color(row_visit, col_visit, board, visited))

    # if have gotten here, need to iterate through everything
    # and mark it as black
    for pos in to_mark:
        row_mark, col_mark = pos
        board[row_mark][col_mark] = 'B'


def get_adjacent_color(row, col, matrix, visited):
    adjacent = []

    # above
    if matrix[row - 1][col] == 'W' and not visited[row - 1][col]:
        adjacent.append((row - 1, col))

    # below
    if matrix[row + 1][col] == 'W' and not visited[row + 1][col]:
        adjacent.append((row + 1, col))

    # left
    if matrix[row][col - 1] == 'W' and not visited[row][col - 1]:
        adjacent.append((row, col - 1))

    # right
    if matrix[row][col + 1] == 'W' and not visited[row][col + 1]:
        adjacent.append((row, col + 1))

    return adjacent
