# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands

- Run any algorithm script: `python wayslearn/<filename>.py`
  - Example: `python wayslearn/dijkstra.py` to execute Dijkstra's algorithm
  - Example: `python wayslearn/floyd.py` to execute Floyd's algorithm
- Install required dependencies: `pip install numpy`

## Code Architecture

This repository contains educational implementations of various algorithms organized by date:

- **Root directory**: Contains the main algorithm collection
- **wayslearn/**: Primary directory for all algorithm implementations
  - **wayslearn/**: Core algorithm implementations (Dijkstra, Floyd, Kruskal, etc.)
  - **wayslearn/4_12/**: April 12 implementations (Kruskal, NIHE variants)
  - **wayslearn/4_13/**: April 13 implementations (logistic regression, goal programming)
  - **wayslearn/4_14/**: April 14 implementations (time series analysis, file reading, score processing)

Each Python file is self-contained with its own implementation and test data. Most algorithms use standard libraries, though some (like `floyd.py`) require NumPy.

The code follows a pattern where:
- Graph algorithms typically define adjacency lists with `add()` functions
- Mathematical algorithms often include sample input data directly in the script
- Files are organized chronologically within the `wayslearn/` directory

When modifying existing algorithms, preserve the sample data structure while updating the implementation logic.