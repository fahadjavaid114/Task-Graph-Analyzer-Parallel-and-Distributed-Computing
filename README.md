# Task Graph Analyzer

A Python-based tool for analyzing weighted task dependency graphs, identifying critical paths, and visualizing parallel execution schedules.

## Features

- Identify starting and finishing tasks in a dependency graph.
- Find all start-to-finish paths and calculate their lengths.
- Determine the critical path and total workload.
- Calculate average and maximum concurrency.
- Compute earliest possible start and finish times.
- Simulate task scheduling across 1, 2, and 3 processors.
- Calculate parallel execution speedup.
- Generate Gantt charts using Matplotlib.

## Technologies Used

- Python
- Matplotlib
- Graph Algorithms
- Parallel Scheduling

## Installation

Install the required dependency:

```bash
pip install matplotlib
```

## Usage

Run the program:

```bash
python task_graph_analyzer.py
```

The program analyzes three example dependency graphs and displays execution results, processor schedules, and Gantt chart visualizations.

## Project Structure

- `task_graph_analyzer.py` — Main Python implementation
- `output.txt` — Sample program output
- `charts/` — Generated Gantt chart visualizations

## Applications

This project demonstrates concepts used in parallel computing, dependency scheduling, workflow management, and database query execution planning.
