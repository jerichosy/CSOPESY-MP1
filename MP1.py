from typing import Dict, List


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
    time_slices = []
    current_time = processes[0].arrival_time
    remaining_time = {}
    last_stop_time: Dict[int, int] = {}

    for process in processes:
        remaining_time[process.pid] = process.burst_time
        last_stop_time[process.pid] = process.arrival_time

    ready_queue.append(processes[0])

    while sum(remaining_time.values()) > 0 and len(processes) > 0:
        if len(ready_queue) == 0 and len(processes) > 0:
            ready_queue.append(processes[0])
            current_time = ready_queue[0].arrival_time

        process_to_execute = ready_queue[0]

        if remaining_time[process_to_execute.pid] <= time_quantum:
            remaining_t = remaining_time[process_to_execute.pid]
            remaining_time[process_to_execute.pid] -= remaining_t
            prev_current_time = current_time
            current_time += remaining_t

            time_slices.append(
                (
                    process_to_execute.pid,
                    prev_current_time,
                    current_time,
                    prev_current_time
                    - last_stop_time[process_to_execute.pid],  # updated waiting time
                )
            )

            last_stop_time[
                process_to_execute.pid
            ] = current_time  # update the stop time
        else:
            remaining_time[process_to_execute.pid] -= time_quantum
            prev_current_time = current_time
            current_time += time_quantum

            time_slices.append(
                (
                    process_to_execute.pid,
                    prev_current_time,
                    current_time,
                    prev_current_time
                    - last_stop_time[process_to_execute.pid],  # updated waiting time
                )
            )

            last_stop_time[
                process_to_execute.pid
            ] = current_time  # update the stop time

        process_to_arrive_in_this_cycle = [
            p
            for p in processes
            if p.arrival_time <= current_time
            and p != process_to_execute
            and p not in ready_queue
            and p in processes
        ]

        ready_queue.extend(process_to_arrive_in_this_cycle)
        ready_queue.append(ready_queue.pop(0))

        if remaining_time[process_to_execute.pid] == 0:
            processes.remove(process_to_execute)
            ready_queue.remove(process_to_execute)

    return time_slices


# Table 1. CPU Scheduling Algorithms and their corresponding value of X.
# | CPU Scheduling Algorithm | Value of X
# |     FCFS	             |     0
# |     SJF	                 |     1
# |     SRTF	             |     2
# |     RR	                 |     3


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

    if X == 0:
        time_slices = FCFS(processes)
    elif X == 1:
        SJF()
    elif X == 2:
        SRTF()
    elif X == 3:
        time_slices = RR(processes, Z)

    # print(result)

    total_waiting_time_by_pid = {}
    for time_slice in time_slices:
        pid = time_slice[0]
        waiting_time = time_slice[3]

        if pid not in total_waiting_time_by_pid:
            total_waiting_time_by_pid[pid] = 0

        total_waiting_time_by_pid[pid] += waiting_time

        print(
            f"{pid} start time: {time_slice[1]} end time: {time_slice[2]} | Waiting time: {waiting_time}"
        )

    avg_waiting_time = sum(total_waiting_time_by_pid.values()) / Y
    print(f"Average waiting time: {avg_waiting_time}")
