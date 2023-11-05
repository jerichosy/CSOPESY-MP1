import bisect
from typing import Dict, List

from utils.utils import Algorithm


class Process:
    def __init__(self, pid, arrival_time, burst_time):
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

    ready_queue = []
    pending_processes = processes.copy()

    time_slices = []
    current_time = processes[0].arrival_time
    total_remaining_time = sum([process.burst_time for process in processes])
    last_stop_time: Dict[int, int] = {}
    remaining_time = {}

    for process in processes:
        remaining_time[process.pid] = process.burst_time
        last_stop_time[process.pid] = process.arrival_time

    idx = bisect.bisect(
        [process.arrival_time for process in pending_processes], current_time
    )
    ready_queue.extend(pending_processes[:idx])
    pending_processes = pending_processes[idx:]  # processes that haven't arrived yet

    while total_remaining_time > 0:
        if len(ready_queue) == 0:
            current_time = pending_processes[0].arrival_time
            idx = bisect.bisect(
                [process.arrival_time for process in pending_processes], current_time
            )
            ready_queue.extend(pending_processes[:idx])
            pending_processes = pending_processes[idx:]

        process_to_execute = ready_queue[0]
        prev_current_time = current_time

        if remaining_time[process_to_execute.pid] <= time_quantum:
            current_time += remaining_time[process_to_execute.pid]
            total_remaining_time -= remaining_time[process_to_execute.pid]
            remaining_time[process_to_execute.pid] = 0
        else:
            current_time += time_quantum
            remaining_time[process_to_execute.pid] -= time_quantum
            total_remaining_time -= time_quantum

        idx = bisect.bisect(
            [process.arrival_time for process in pending_processes], current_time
        )
        ready_queue.extend(pending_processes[:idx])
        pending_processes = pending_processes[idx:]

        time_slices.append(
            (
                process_to_execute.pid,
                prev_current_time,
                current_time,
                prev_current_time - last_stop_time[process_to_execute.pid],
            )
        )

        last_stop_time[process_to_execute.pid] = current_time

        if remaining_time[process_to_execute.pid] == 0:
            ready_queue.remove(process_to_execute)

        else:
            ready_queue.append(ready_queue.pop(0))

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
    total_waiting_time_by_pid = {}
    formatted = []
    for time_slice in time_slices:
        pid = time_slice[0]
        waiting_time = time_slice[3]

        if pid not in total_waiting_time_by_pid:
            total_waiting_time_by_pid[pid] = 0

        total_waiting_time_by_pid[pid] += waiting_time

        formatted.append(
            f"{pid} start time: {time_slice[1]} end time: {time_slice[2]} | Waiting time: {waiting_time}"
        )

    avg_waiting_time = sum(total_waiting_time_by_pid.values()) / Y
    formatted.append(f"Average waiting time: {round(avg_waiting_time, 1)}")

    return "\n".join(formatted)


if __name__ == "__main__":
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

    print(format_result(time_slices, Y), end="")
