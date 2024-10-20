from Maze2 import Maze
from graph import Graph
from dfs import DFS
from bfs import BFS


def generate_graph(maze):
    graph = Graph()
    for row in range(maze.y_size):
        for col in range(maze.x_size):
            if maze.maze[row][col].side(1):
                node1 = row * maze.x_size + col
                node2 = row * maze.x_size + col + 1
                graph.add_edge(node1, node2)
            if maze.maze[row][col].side(2):
                node1 = row * maze.x_size + col
                node2 = (row + 1) * maze.x_size + col
                graph.add_edge(node1, node2)
    return graph


def dfs_solve(maze):
    graph = generate_graph(maze)
    end = maze.y_size * maze.x_size - 1
    dfs = DFS(graph, 0)
    print(dfs.path_to(end))


def bfs_solve(maze):
    graph = generate_graph(maze)
    end = maze.y_size * maze.x_size - 1
    bfs = BFS(graph, 0)
    print(bfs.path_to(end))


if __name__ == '__main__':
    maze = Maze(3, 3)
    print(maze)
    dfs_solve(maze)
    bfs_solve(maze)
