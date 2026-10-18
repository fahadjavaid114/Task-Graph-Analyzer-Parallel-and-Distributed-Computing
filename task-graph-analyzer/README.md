# \# Task Graph Analyzer

# 

# A Python-based tool for analyzing weighted task dependency graphs, identifying critical paths, evaluating parallelism, and visualizing task execution across multiple processors.

# 

# \## Overview

# 

# Task Graph Analyzer explores how dependent tasks can be scheduled and executed efficiently using parallel computing techniques.

# 

# The project analyzes three example task graphs, including a general workflow and two alternative database query execution plans. It calculates scheduling metrics, evaluates processor utilization, and generates Gantt charts to visualize execution.

# 

# \## Features

# 

# \- \*\*Graph Analysis:\*\* Identify starting and finishing nodes in directed acyclic graphs (DAGs).

# \- \*\*Path Analysis:\*\* Find all start-to-finish paths and calculate their lengths.

# \- \*\*Critical Path Detection:\*\* Determine the longest dependency path.

# \- \*\*Workload Analysis:\*\* Calculate total computational work.

# \- \*\*Concurrency Analysis:\*\* Calculate average and maximum concurrency.

# \- \*\*ASAP Scheduling:\*\* Determine earliest possible start and finish times.

# \- \*\*Processor Scheduling:\*\* Simulate task execution using 1, 2, and 3 processors.

# \- \*\*Performance Evaluation:\*\* Calculate execution times and speedup.

# \- \*\*Gantt Chart Visualization:\*\* Generate visual timelines of task execution.

# 

# \## Technologies Used

# 

# \- Python 3

# \- Matplotlib

# \- Directed Acyclic Graphs (DAGs)

# \- Graph Traversal Algorithms

# \- Parallel Task Scheduling

# 

# \## Project Structure

# 

# ```text

# task-graph-analyzer/

# │

# ├── task\_graph\_analyzer.py

# ├── README.md

# ├── sample\_output.txt

# │

# └── charts/

# &#x20;   ├── workflow\_p1.png

# &#x20;   ├── workflow\_p2.png

# &#x20;   ├── workflow\_p3.png

# &#x20;   ├── query\_plan\_a\_p1.png

# &#x20;   ├── query\_plan\_a\_p2.png

# &#x20;   ├── query\_plan\_a\_p3.png

# &#x20;   ├── query\_plan\_b\_p1.png

# &#x20;   ├── query\_plan\_b\_p2.png

# &#x20;   └── query\_plan\_b\_p3.png

# ```

# 

# \## Installation

# 

# \*\*1. Clone the repository\*\*

# 

# ```bash

# git clone https://github.com/YOUR\_USERNAME/task-graph-analyzer.git

# ```

# 

# \*\*2. Navigate to the project folder\*\*

# 

# ```bash

# cd task-graph-analyzer

# ```

# 

# \*\*3. Install dependencies\*\*

# 

# ```bash

# pip install matplotlib

# ```

# 

# \## Usage

# 

# Run the Python program:

# 

# ```bash

# python task\_graph\_analyzer.py

# ```

# 

# The program analyzes three predefined task graphs:

# 

# 1\. \*\*Workflow Graph:\*\* A weighted task dependency network.

# 2\. \*\*Query Plan A:\*\* A database query execution workflow.

# 3\. \*\*Query Plan B:\*\* An alternative execution order for the same query.

# 

# For each graph, the program calculates scheduling metrics and evaluates execution using different processor counts.

# 

# Sample console results are available in `sample\_output.txt`, and execution visualizations are stored in the `charts/` directory.

# 

# \## Performance Analysis

# 

# The tool calculates several performance metrics.

# 

# \*\*Total Work (W)\*\*

# 

# The sum of execution costs of all tasks.

# 

# \*\*Critical Path Length (L)\*\*

# 

# The longest weighted dependency path from a starting task to a finishing task.

# 

# \*\*Average Concurrency\*\*

# 

# ```text

# Average Concurrency = Total Work / Critical Path Length

# ```

# 

# \*\*Speedup\*\*

# 

# ```text

# Speedup = Sequential Execution Time / Parallel Execution Time

# ```

# 

# \### Example Results

# 

# | Graph | Total Work | Critical Path | 1 Processor | 2 Processors | 3 Processors |

# |---|---:|---:|---:|---:|---:|

# | Workflow | 37 | 17 | 37 | 23 | 17 |

# | Query Plan A | 74 | 35 | 74 | 45 | 42 |

# | Query Plan B | 75 | 45 | 75 | 55 | 55 |

# 

# These results demonstrate how task dependencies and execution order influence parallel performance.

# 

# \## Gantt Chart Visualizations

# 

# The program generates Gantt charts to illustrate task execution across different processor configurations.

# 

# \### Workflow Graph

# 

# !\[Workflow with 2 Processors](charts/workflow\_p2.png)

# 

# \### Query Plan A

# 

# !\[Query Plan A with 2 Processors](charts/query\_plan\_a\_p2.png)

# 

# \### Query Plan B

# 

# !\[Query Plan B with 2 Processors](charts/query\_plan\_b\_p2.png)

# 

# Additional Gantt charts for 1 and 3 processors are available in the `charts/` directory.

# 

# \## Key Concepts Demonstrated

# 

# \- Task dependency management

# \- Critical path analysis

# \- Parallel execution scheduling

# \- Processor allocation

# \- Work and span analysis

# \- Performance benchmarking

# \- Database query execution planning

# 

# \## Potential Applications

# 

# The concepts demonstrated in this project are relevant to:

# 

# \- Parallel and distributed computing

# \- Workflow automation

# \- Job scheduling systems

# \- Database query optimization

# \- Resource allocation

# \- Project scheduling

# 

# \## Future Improvements

# 

# Potential enhancements include:

# 

# \- Support for user-defined task graphs

# \- Additional scheduling algorithms

# \- Interactive graph visualization

# \- Scheduling with configurable processor counts

# \- Comparison of scheduling heuristics

# 

# \## Author

# 

# Developed by \*\*Fahad Javaid\*\*.

# 

# \## License

# 

# No license has been specified for this project.

