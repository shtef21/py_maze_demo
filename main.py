from pyamaze import maze
from queue import PriorityQueue

# Heuristics will be calculated as Euclidian (air) distance
def distance(cell1, cell2):
  x1, y1 = cell1
  x2, y2 = cell2
  return abs(x1-x2) + abs(y1-y2)


# A star algoritm:
#   f(node) = g(node) + h(node)
def a_star(maze):

  # Start is at the bottom-right corner
  start = (maze.rows, maze.cols)
  finish = (1, 1)
  
  # Initialize f and g costs
  g_score = { cell: float('inf') for cell in maze.grid }
  g_score[start] = 0
  f_score = { cell: float('inf') for cell in maze.grid }
  f_score[start] = g_score[start] + distance(start, finish)

  # Create a search container
  #   Priority queue takes lowest value first
  open=PriorityQueue()
  open.put((
    f_score[start],
    distance(start, finish),
    start,
  ))

  # Start searching in all directions until end found or queue empty
  while not open.empty():
    # Take item with lowest f_score (first element of the tuple)
    currCell = open.get()[2]

    # If best path to finish reached
    if currCell == finish:
      break

    # Go in all directions that aren't blocked by walls
    for d in 'ESNW':
      if maze.maze_map[currCell][d] == True:
        if d == 'E':
          next_cell = (currCell[0], currCell[1]+1)
        elif d == 'W':
          next_cell = (currCell[0], currCell[1]-1)
        elif d == 'N':
          next_cell = (currCell[0]-1, currCell[1])
        elif d == 'S':
          next_cell = (currCell[0]+1, currCell[1])

        # Calculate F and G of this path
        temp_g_score = g_score[currCell] + 1
        temp_h_score = distance(next_cell, finish)
        temp_f_score = temp_g_score + temp_h_score

        # Save costs if they are smaller
        # than previous costs to next_cell
        if temp_f_score < f_score[next_cell]:
          g_score[next_cell] = temp_g_score
          f_score[next_cell] = temp_f_score

          # Expand this path in future iterations
          open.put((temp_f_score, temp_h_score, next_cell))

  print(f'{g_score=}')
  print(f'{f_score=}')

# Create maze
m=maze(5,5)
m.CreateMaze()

# Run A* algorithm
a_star(m)

# Show the maze
m.run()
