import argparse
from pathlib import Path


STUDENTS = [
    (101, 'CS', 2023, 'Lahore'),
    (102, 'EE', 2023, 'Faisalabad'),
    (103, 'CS', 2022, 'Faisalabad'),
    (104, 'CS', 2023, 'Faisalabad'),
    (105, 'SE', 2023, 'Lahore'),
    (106, 'CS', 2023, 'Karachi'),
    (107, 'CS', 2021, 'Lahore'),
    (108, 'EE', 2022, 'Lahore'),
    (109, 'CS', 2023, 'Lahore'),
    (110, 'SE', 2022, 'Faisalabad'),
]


def task_order(task):
    return int(task[1:])


def question_2():
    weights = {'T1': 4, 'T2': 6, 'T3': 3, 'T4': 5, 'T5': 2,
               'T6': 8, 'T7': 3, 'T8': 4, 'T9': 2}
    predecessors = {
        'T1': [], 'T2': [], 'T3': [],
        'T4': ['T1', 'T2'], 'T5': ['T2'], 'T6': ['T3'],
        'T7': ['T4', 'T5'], 'T8': ['T5', 'T6'],
        'T9': ['T7', 'T8'],
    }
    return 'Question 2: Task Dependency Graph', weights, predecessors, {}


def question_3(alternate=False):
    cs = {sid for sid, dept, year, city in STUDENTS if dept == 'CS'}
    year = {sid for sid, dept, batch, city in STUDENTS if batch == 2023}
    lahore = {sid for sid, dept, batch, city in STUDENTS if city == 'Lahore'}
    faisalabad = {sid for sid, dept, batch, city in STUDENTS if city == 'Faisalabad'}

    rows = {'T1': cs, 'T2': year, 'T3': lahore, 'T4': faisalabad}
    names = {
        'T1': 'CS', 'T2': '2023', 'T3': 'Lahore', 'T4': 'Faisalabad'
    }
    weights = {task: 10 for task in rows}
    predecessors = {task: [] for task in rows}

    def combine(task, first, second, operation, label):
        predecessors[task] = [first, second]
        weights[task] = len(rows[first]) + len(rows[second])
        rows[task] = rows[first] & rows[second] if operation == 'AND' else rows[first] | rows[second]
        names[task] = label

    if not alternate:
        combine('T5', 'T1', 'T2', 'AND', 'CS AND 2023')
        combine('T6', 'T3', 'T4', 'OR', 'Lahore OR Faisalabad')
        combine('T7', 'T5', 'T6', 'AND', 'Final result')
        title = 'Question 3(a): (CS AND 2023) AND (Lahore OR Faisalabad)'
    else:
        combine('T5', 'T3', 'T4', 'OR', 'Lahore OR Faisalabad')
        combine('T6', 'T5', 'T2', 'AND', '(Lahore OR Faisalabad) AND 2023')
        combine('T7', 'T6', 'T1', 'AND', 'Final result')
        title = 'Question 3(b): ((Lahore OR Faisalabad) AND 2023) AND CS'

    info = {task: (names[task], sorted(rows[task])) for task in rows}
    return title, weights, predecessors, info


def graph_analysis(weights, predecessors):
    tasks = sorted(weights, key=task_order)
    if set(weights) != set(predecessors):
        raise ValueError('Every task must have a predecessor entry.')
    successors = {task: [] for task in tasks}
    for task in tasks:
        for predecessor in predecessors[task]:
            successors[predecessor].append(task)
    starts = [task for task in tasks if not predecessors[task]]
    finishes = [task for task in tasks if not successors[task]]

    paths = []

    def explore(task, path):
        path = path + [task]
        if task in finishes:
            paths.append((path, sum(weights[item] for item in path)))
        for next_task in sorted(successors[task], key=task_order):
            explore(next_task, path)

    for start in starts:
        explore(start, [])

    asap = {}
    pending = set(tasks)
    while pending:
        ready = sorted((task for task in pending
                        if all(item in asap for item in predecessors[task])), key=task_order)
        if not ready:
            raise ValueError('The task graph has a cycle.')
        for task in ready:
            begin = max((asap[item][1] for item in predecessors[task]), default=0)
            asap[task] = (begin, begin + weights[task])
            pending.remove(task)

    critical_length = max(length for path, length in paths)
    critical_paths = [path for path, length in paths if length == critical_length]
    events = sorted({time for begin, end in asap.values() for time in (begin, end)})
    intervals = []
    for begin, end in zip(events, events[1:]):
        count = sum(start <= begin < finish for start, finish in asap.values())
        if begin < end:
            intervals.append((begin, end, count))
    maximum = max(count for begin, end, count in intervals)
    maximum_intervals = []
    for begin, end, count in intervals:
        if count != maximum:
            continue
        if maximum_intervals and maximum_intervals[-1][1] == begin:
            maximum_intervals[-1] = (maximum_intervals[-1][0], end)
        else:
            maximum_intervals.append((begin, end))

    return starts, finishes, paths, critical_paths, critical_length, asap, maximum, maximum_intervals


def schedule_processors(weights, predecessors, processor_count):
    pending = set(weights)
    completed = set()
    running = {}
    schedule = []
    current_time = 0

    while pending or running:
        for processor in range(1, processor_count + 1):
            if processor in running and running[processor][1] == current_time:
                completed.add(running.pop(processor)[0])

        for processor in range(1, processor_count + 1):
            if processor in running:
                continue
            ready = sorted((task for task in pending
                            if all(item in completed for item in predecessors[task])),
                           key=task_order)
            if ready:
                task = ready[0]
                finish = current_time + weights[task]
                schedule.append((processor, task, current_time, finish))
                running[processor] = (task, finish)
                pending.remove(task)

        if not running:
            if not pending:
                break
            raise ValueError('Cannot schedule remaining tasks (cycle or missing prerequisite).')
        current_time = min(finish for task, finish in running.values())

    return schedule, current_time


def print_graph(graph):
    title, weights, predecessors, info = graph
    (starts, finishes, paths, critical_paths, critical_length,
     asap, maximum, maximum_intervals) = graph_analysis(weights, predecessors)
    total_work = sum(weights.values())
    separator = '=' * 76
    print('\n' + separator)
    print(title)
    print(separator)
    print('Task weights, predecessors' + (', and row IDs' if info else ''))
    for task in sorted(weights, key=task_order):
        predecessors_text = ', '.join(predecessors[task]) or 'none'
        print(f'  {task}: cost={weights[task]:2d}, predecessors=[{predecessors_text}]', end='')
        if info:
            name, ids = info[task]
            print(f', table={name}, IDs={ids}', end='')
        print()

    print('\n1. Start nodes:', ', '.join(starts))
    print('   Finish nodes:', ', '.join(finishes))
    print('\n2. All start-to-finish paths (sum of task costs):')
    for path, length in paths:
        marker = ' [CRITICAL]' if length == critical_length else ''
        print(f'   {" -> ".join(path)}: {length}{marker}')
    print('   Critical path(s):', '; '.join(' -> '.join(path) for path in critical_paths))
    print('   Critical-path length:', critical_length)

    print('\n3. Total work:', total_work)
    print(f'   Average degree of concurrency: {total_work}/{critical_length} = {total_work / critical_length:.4f}')

    print('\n4. Unlimited-processor ASAP start/finish times:')
    for task in sorted(weights, key=task_order):
        print(f'   {task}: [{asap[task][0]}, {asap[task][1]})')
    print('   Maximum concurrent tasks:', maximum)
    print('   Interval(s) of maximum concurrency:',
          ', '.join(f'[{start}, {end})' for start, end in maximum_intervals))

    print('\n5. Non-preemptive schedules: lowest-numbered READY task; P1, then P2, then P3')
    critical_tasks = {task for path in critical_paths for task in path}
    schedules = {}
    for processors in (1, 2, 3):
        schedule, duration = schedule_processors(weights, predecessors, processors)
        schedules[processors] = schedule
        print(f'   p={processors}: total time={duration}, speedup={total_work}/{duration} = {total_work / duration:.4f}')
        print('     Processor  Task  Start  End')
        for processor, task, start, end in schedule:
            print(f'     P{processor:<9} {task:<5} {start:<6} {end}')

    if info:
        print('\n   Final matching student IDs:', info['T7'][1])
    return title, schedules, critical_tasks


def draw_gantt(title, schedule, critical_tasks, processors, filename):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import Patch

    fig, ax = plt.subplots(figsize=(10, max(2.5, processors * 1.25 + 1)))
    for processor, task, start, end in schedule:
        color = '#D35151' if task in critical_tasks else '#4474AF'
        ax.barh(processor, end - start, left=start, height=0.58,
                color=color, edgecolor='white', linewidth=1)
        ax.text((start + end) / 2, processor, task, va='center', ha='center',
                color='white', fontsize=10, fontweight='bold')
    end_time = max(end for _, _, _, end in schedule)
    ax.set_yticks(list(range(1, processors + 1)))
    ax.set_yticklabels([f'P{p}' for p in range(1, processors + 1)])
    ax.invert_yaxis()
    ax.set_xlim(0, end_time + 1)
    ax.set_xlabel('Time units')
    ax.set_ylabel('Processor')
    ax.set_title(f'{title}\np={processors} | Total time={end_time}')
    ax.grid(axis='x', alpha=0.25)
    ax.set_axisbelow(True)
    ax.legend(handles=[Patch(color='#D35151', label='Critical-path task'),
                       Patch(color='#4474AF', label='Other task')], loc='lower right')
    fig.tight_layout()
    fig.savefig(filename, dpi=150)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description='Q9: Analyze all three task graphs.')
    parser.add_argument('--no-charts', action='store_true', help='Print output without Gantt charts')
    parser.add_argument('--charts-dir', default='charts', help='Folder for PNG charts (default: charts)')
    args = parser.parse_args()

    graphs = [question_2(), question_3(), question_3(alternate=True)]
    for i, graph in enumerate(graphs):
        title, schedules, critical_tasks = print_graph(graph)
        if not args.no_charts:
            output_dir = Path(args.charts_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
            for processors, schedule in schedules.items():
                filename = output_dir / f'graph_{i + 1}_p{processors}.png'
                draw_gantt(title, schedule, critical_tasks, processors, filename)
    print('\nDone. All three graphs analyzed.' +
          ('' if args.no_charts else f' Gantt charts are in: {args.charts_dir}/'))


if __name__ == '__main__':
    main()
