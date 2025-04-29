from algorithms import Process, srtf_scheduler, hrrn_scheduler, fcfs_scheduler
from graphing import plot_avg_times, plot_cpu_utilization, plot_throughput, print_results
import copy
# Example process set
processes = [
    Process(pid=1, arrival_time=0, burst_time=8),
    Process(pid=2, arrival_time=1, burst_time=4),
    Process(pid=3, arrival_time=2, burst_time=9),
    Process(pid=4, arrival_time=3, burst_time=5),
]
cpu_utils = {}
throughputs = {}
avg_times = {}
# FCFS
fcfs_processes, fcfs_gantt = fcfs_scheduler(copy.deepcopy(processes))
fcfs_awt, fcfs_att, fcfs_cpu_util, fcfs_throughput = print_results(fcfs_processes, fcfs_gantt, "FCFS")
avg_times["FCFS"] = {'AWT': fcfs_awt, 'ATT': fcfs_att}
cpu_utils["FCFS"] = fcfs_cpu_util
throughputs["FCFS"] = fcfs_throughput

# SRTF
srtf_processes, srtf_gantt = srtf_scheduler(copy.deepcopy(processes))
srtf_awt, srtf_att, srtf_cpu_util, srtf_throughput = print_results(srtf_processes, srtf_gantt, "SRTF")
avg_times["SRTF"] = {'AWT': srtf_awt, 'ATT': srtf_att}
cpu_utils["SRTF"] = srtf_cpu_util
throughputs["SRTF"] = srtf_throughput

# HRRN
hrrn_processes, hrrn_gantt = hrrn_scheduler(copy.deepcopy(processes))
hrrn_awt, hrrn_att, hrrn_cpu_util, hrrn_throughput = print_results(hrrn_processes, hrrn_gantt, "HRRN")
avg_times["HRRN"] = {'AWT': hrrn_awt, 'ATT': hrrn_att}
cpu_utils["HRRN"] = hrrn_cpu_util
throughputs["HRRN"] = hrrn_throughput

plot_avg_times(avg_times)
#plot_cpu_utilization(cpu_utils)
#plot_throughput(throughputs)