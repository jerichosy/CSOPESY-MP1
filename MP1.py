import argparse
import bisect
from collections import deque
from typing import Dict, List

from utils.utils import Algorithm


class Process:
    def __init__(self, pid, arrival_time, burst_time):
        # These values are not mutated over the course of the algorithm
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time


def FCFS(processes: List[Process]):
    processes.sort(key=lambda Process: Process.arrival_time)

    time_slices = []
    previous_end_time = processes[0].arrival_time
    for process in processes:
        # start, end, waiting
        time_slices.append(
            (
                process.pid,
                previous_end_time,
                previous_end_time + process.burst_time,
                previous_end_time - process.arrival_time,  # waiting time
            )
        )
        previous_end_time += process.burst_time
    return time_slices


def SJF():
    raise NotImplementedError


def SRTF():
    raise NotImplementedError


def RR(processes: List[Process], time_quantum: int):
    processes.sort(key=lambda Process: Process.arrival_time)

    ready_queue = deque()
    pending_processes = processes.copy()

    time_slices = []
    total_remaining_time = sum([process.burst_time for process in processes])
    last_stop_time: Dict[int, int] = {}  # for time slice
    remaining_time = {}

    for process in processes:
        remaining_time[process.pid] = process.burst_time
        last_stop_time[process.pid] = process.arrival_time  # for time slice

    # Execute processes until all processes are completed
    while total_remaining_time > 0:
        # If ready queue is empty, advance time to next process arrival
        # Happens at the start of the algorithm and when arrival time of next process is greater than current time
        if not ready_queue:
            current_time = pending_processes[0].arrival_time
            idx = bisect.bisect(
                pending_processes,
                current_time,
                key=lambda Process: Process.arrival_time,
            )
            ready_queue.extend(pending_processes[:idx])  # processes that have arrived
            pending_processes = pending_processes[idx:]

        process_to_execute = ready_queue[0]
        prev_current_time = current_time  # for time slice

        # Execute process until completion or for time quantum
        if remaining_time[process_to_execute.pid] <= time_quantum:
            # If process is completed within time quantum, execute for remaining time
            current_time += remaining_time[process_to_execute.pid]
            total_remaining_time -= remaining_time[process_to_execute.pid]
            remaining_time[process_to_execute.pid] = 0
        else:
            # If process will not be completed within time quantum, execute for time quantum
            current_time += time_quantum
            remaining_time[process_to_execute.pid] -= time_quantum
            total_remaining_time -= time_quantum

        # Add processes that have arrived while current process was executing
        idx = bisect.bisect(
            pending_processes,
            current_time,
            key=lambda Process: Process.arrival_time,
        )
        ready_queue.extend(pending_processes[:idx])  # processes that have arrived
        pending_processes = pending_processes[idx:]

        # Record time slice
        time_slices.append(
            (
                process_to_execute.pid,
                prev_current_time,
                current_time,
                prev_current_time - last_stop_time[process_to_execute.pid],
            )
        )
        # To calculate waiting time when process is resumed after being preempted (paused)
        # Set last stop time to current time when process is preempted (paused)
        last_stop_time[process_to_execute.pid] = current_time  # for time slice

        if remaining_time[process_to_execute.pid] == 0:
            # Remove process from ready queue if it is completed
            ready_queue.remove(process_to_execute)
        else:
            # Move process to back of ready queue if it is not completed
            ready_queue.append(ready_queue.popleft())

    return time_slices


# Table 1. CPU Scheduling Algorithms and their corresponding value of X.
# | CPU Scheduling Algorithm | Value of X
# |     FCFS	             |     0
# |     SJF	                 |     1
# |     SRTF	             |     2
# |     RR	                 |     3
def solve(algorithm: Algorithm, processes: List[Process], Z: int):
    if algorithm == Algorithm.FCFS:
        return FCFS(processes)
    elif algorithm == Algorithm.SJF:
        SJF()
    elif algorithm == Algorithm.SRTF:
        SRTF()
    elif algorithm == Algorithm.RR:
        return RR(processes, Z)


def format_result(time_slices: List[tuple], Y: int):
    process_time_slices = {}
    formatted = []

    # Group time slices by process ID
    for time_slice in time_slices:
        pid, start_time, end_time, waiting_time = time_slice
        if pid not in process_time_slices:
            process_time_slices[pid] = {"time_slices": [], "total_waiting_time": 0}

        process_time_slices[pid]["time_slices"].append(
            f"start time: {start_time} end time: {end_time}"
        )
        process_time_slices[pid]["total_waiting_time"] += waiting_time

    # Format output for each process
    for pid in sorted(process_time_slices.keys()):
        slices_str = " | ".join(process_time_slices[pid]["time_slices"])
        waiting_time = process_time_slices[pid]["total_waiting_time"]
        formatted.append(f"{pid} {slices_str} | Waiting time: {waiting_time}")

    # Calculate average waiting time
    total_waiting_time = sum(
        value["total_waiting_time"] for value in process_time_slices.values()
    )
    avg_waiting_time = total_waiting_time / Y
    formatted.append(f"Average waiting time: {round(avg_waiting_time, 1)}")

    return "\n".join(formatted)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--silent", action="store_true", help="Suppress algorithm output"
    )
    args = parser.parse_args()

    # X = CPU scheduling algorithm
    # Y = number of processes (constraints: 3 ≤ Y ≤ 100)
    # Z = time slice value (constraints: 1 ≤ Z ≤ 100, applicable to Round-Robin only, if X is not RR then this must be set 1 and ignored)
    X, Y, Z = list(map(int, input().rstrip().split(" ")))
    processes = []
    for _ in range(Y):
        # A = process ID
        # B = arrival time
        # C = burst time
        A, B, C = list(map(int, input().rstrip().split(" ")))
        processes.append(Process(A, B, C))

    time_slices = solve(Algorithm(X), processes, Z)

    if not args.silent:
        print(format_result(time_slices, Y), end="")
