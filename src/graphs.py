# Const values for maze problem

WHITE = 'WHITE'
BLACK = 'BLACK'

class Visited(object):
    def __init__(self, point, neighbors, pos):
        self.point = point
        self.neighbors = neighbors
        self.pos = pos

def search_maze(maze, start, end):
    '''
    Question 19.1: Given a 2d array of black and white entries representing
    a maze with designated entrance and exit points, find a path from the
    entrance to the exit.
    '''
    path = []
    has_neighbors = [start]
    visited = {
        start: Visited(
            start,
            get_neighbors(start),
            len(path)-1,
        )
    }

    while has_neighbors:
        pt = has_neighbors[-1]
        neighbor = visited[pt].pop()
        while 
        break
    return 

def get_neighbors(point, maze):
    neighbors = []
    print('point: {}'.format(point))
    print('maze: {} rows, {} cols'.format(len(maze),len(maze[0])))

    # get point below
    if point[0] > 0:
        row, col = point[0]-1, point[1]
        print('below is {}: {}'.format((row,col),maze[row][col]))
        if maze[row][col] == WHITE:
            neighbors.append((row,col))

    # get point above
    if point[0] < len(maze) - 1:
        row, col = point[0]+1, point[1]
        print('above is {}: {}'.format((row,col),maze[row][col]))
        if maze[row][col] == WHITE:
            neighbors.append((row,col))

    # get point on left
    if point[1] > 0:
        row, col = point[0], point[1]-1
        print('left is {}: {}'.format((row,col),maze[row][col]))
        if maze[row][col] == WHITE:
            neighbors.append((row,col))

    # get point on right
    if point[1] < len(maze[0]) - 1:
        row, col = point[0], point[1]+1
        print('right is {}: {}'.format((row,col),maze[row][col]))
        if maze[row][col] == WHITE:
            neighbors.append((row,col))

    return neighbors
