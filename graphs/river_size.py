"""
River Sizes
You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only 0s and 1s. Each 0 represents land, and each 1 represents part of a river. A river consists of any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent). The number of adjacent 1s forming a river determine its size.

Note that a river can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal line; it can be L-shaped, for example.

Write a function that returns an array of the sizes of all rivers represented in the input matrix. The sizes don't need to be in any particular order.

Sample Input
matrix = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0],
]
Sample Output
[1, 2, 2, 2, 5] // The numbers could be ordered differently.

// The rivers can be clearly seen here:
// [
//   [1,  ,  , 1,  ],
//   [1,  , 1,  ,  ],
//   [ ,  , 1,  , 1],
//   [1,  , 1,  , 1],
//   [1,  , 1, 1,  ],
// ]

"""
import unittest


def river_sizes(matrix):
    visited = [[False for _ in row] for row in matrix]
    result = []
    # traverse through each node
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not visited[i][j]:
                size = traverse(i, j, matrix, visited)
                if size: result.append(size)

    return result

def traverse(i, j, matrix, visited):
    """
    Traverse the given node in all four directions
    """
    nodes = [[i, j]]
    size = 0
    while nodes:
        node = nodes.pop()
        
        if matrix[node[0]][node[1]] == 0:
            continue
        if visited[node[0]][node[1]]:
            continue

        visited[node[0]][node[1]] = True
        size += 1
        nodes.extend(get_unvisited_neighbours(node[0], node[1], matrix, visited))

    return size


def get_unvisited_neighbours(i, j, matrix, visited):
    """
    Returns all neighbour nodes for i, j

    (i-1, j), (i+1, j), (i, j - 1), (i, j + 1)

    """
    pairs = []
    if i > 0:
        pairs.append([i - 1, j])
    if i < len(matrix) - 1:
        pairs.append([i + 1, j])
    if j > 0:
        pairs.append([i, j - 1])
    if j < len(matrix[0]) - 1:
        pairs.append([i, j + 1])

    return pairs


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        testInput = [[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]]
        expected = [1, 2, 2, 2, 5]
        self.assertEqual(sorted(river_sizes(testInput)), expected)
        print("Program executed sucessfully")

    
TestProgram().test_case_1()