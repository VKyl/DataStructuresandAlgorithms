from Maze2 import Maze
from graph import Graph
from dfs import DFS
from bfs import BFS

import matplotlib.pyplot as plt


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
    print("DFS path:", dfs.path_to(end))


def bfs_solve(maze):
    graph = generate_graph(maze)
    end = maze.y_size * maze.x_size - 1
    bfs = BFS(graph, 0)
    print("BFS path:",  bfs.path_to(end))


def draw_cell(ax, cell, position):
    x, y = position
    side_length = 1

    if not cell.side(0):
        ax.plot([x, x + side_length], [y + side_length, y + side_length], 'k-', lw=2)
    if not cell.side(1):
        ax.plot([x + side_length, x + side_length], [y, y + side_length], 'k-', lw=2)
    if not cell.side(2):
        ax.plot([x, x + side_length], [y, y], 'k-', lw=2)
    if not cell.side(3):
        ax.plot([x, x], [y, y + side_length], 'k-', lw=2)


def draw_grid(maze: Maze):
    fig, ax = plt.subplots(figsize=(maze.x_size, maze.y_size))
    ax.set_xlim(0, maze.x_size)
    ax.set_ylim(0, maze.y_size)

    for row in range(maze.y_size):
        for col in range(maze.x_size):
            cell = maze.maze[row][col]
            draw_cell(ax, cell, (col, maze.y_size - row - 1))

    ax.set_aspect('equal')
    ax.axis('off')
    plt.show()


if __name__ == '__main__':
    maze = Maze(20, 20)
    print(maze)
    draw_grid(maze)
    dfs_solve(maze)
    bfs_solve(maze)
