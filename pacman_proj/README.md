# Search and Adversarial Agents in AI

This project explores search algorithms and adversarial agents in Artificial Intelligence, implemented in Python.

## Features
- **Uninformed Search**: DFS, BFS, and Uniform Cost Search.
- **Informed Search**: A* and heuristic-based search.
- **Adversarial Search**: Minimax, Alpha-Beta Pruning, and Reflex Agent improvements.

## Technology Used
- **Python**: Implementation of search algorithms and AI agents.

## Usage
Run the provided Python scripts to test various search strategies and agent behaviors.

### Testing and Visualization Commands

#### Minimax Agent (Depth 4)
```sh
python3 pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4
```

#### A* Search with Manhattan Heuristic on Big Maze
```sh
python3 pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

#### Alpha-Beta Pruning Agent (Depth 3) on Small Classic Map
```sh
python3 pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic
```

