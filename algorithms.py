class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = None
        self.completion_time = None

def srtf_scheduler(process_list):
    time = 0
    complete = 0
    n = len(process_list)
    ready_queue = []
    gantt_chart = []
    while complete < n:
        for process in process_list:
            if process.arrival_time <= time and process not in ready_queue and process.remaining_time > 0:
                ready_queue.append(process)
        if ready_queue:
            ready_queue.sort(key=lambda p: (p.remaining_time, p.pid))
            current = ready_queue[0]
            if current.start_time is None:
                current.start_time = time
            current.remaining_time -= 1
            gantt_chart.append(current.pid)
            if current.remaining_time == 0:
                current.completion_time = time + 1
                ready_queue.remove(current)
                complete += 1
        else:
            gantt_chart.append('idle')
        time += 1
    return process_list, gantt_chart
def hrrn_scheduler(process_list):
    time = 0
    completed = 0
    n = len(process_list)
    gantt_chart = []
    while completed < n:
        ready_queue = [p for p in process_list if p.arrival_time <= time and p.completion_time is None]
        if ready_queue:
            for process in ready_queue:
                waiting_time = time - process.arrival_time
                response_ratio = (waiting_time + process.burst_time) / process.burst_time
                process.response_ratio = response_ratio
            ready_queue.sort(key=lambda p: (-p.response_ratio, p.pid))
            current = ready_queue[0]
            current.start_time = time
            gantt_chart.extend([current.pid] * current.burst_time)
            time += current.burst_time
            current.completion_time = time
            completed += 1
        else:
            gantt_chart.append('idle')
            time += 1
    return process_list, gantt_chart
def fcfs_scheduler(process_list):
    time = 0
    completed = 0
    gantt_chart = []
    process_list.sort(key=lambda p: (p.arrival_time, p.pid))
    for process in process_list:
        if time < process.arrival_time:
            while time < process.arrival_time:
                gantt_chart.append('idle')
                time += 1
        process.start_time = time
        gantt_chart.extend([process.pid] * process.burst_time)
        time += process.burst_time
        process.completion_time = time
        completed += 1
    return process_list, gantt_chart