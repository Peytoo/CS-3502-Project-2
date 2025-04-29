import matplotlib.pyplot as plt
def print_results(process_list, gantt_chart, algo_name):
    print(f"\n{algo_name} Gantt Chart:")
    print(gantt_chart)
    total_waiting_time = 0
    total_turnaround_time = 0
    total_burst_time = 0
    n = len(process_list)
    print("\nProcess Results:")
    for p in sorted(process_list, key=lambda x: x.pid):
        turnaround_time = p.completion_time - p.arrival_time
        waiting_time = turnaround_time - p.burst_time
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        total_burst_time += p.burst_time
        print(f"PID={p.pid}, Arrival={p.arrival_time}, Burst={p.burst_time}, Start={p.start_time}, Completion={p.completion_time}, Waiting={waiting_time}, Turnaround={turnaround_time}")
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n
    total_time = len(gantt_chart)
    cpu_utilization = (total_burst_time / total_time) * 100
    throughput = n / total_time
    print("\nSummary Metrics:")
    print(f"Average Waiting Time (AWT): {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time (ATT): {avg_turnaround_time:.2f}")
    print(f"CPU Utilization: {cpu_utilization:.2f}%")
    print(f"Throughput: {throughput:.4f} processes/second")
    return avg_waiting_time, avg_turnaround_time, cpu_utilization, throughput
def plot_avg_times(avg_times):
    algorithms = list(avg_times.keys())
    awt_values = [avg_times[algo]['AWT'] for algo in algorithms]
    att_values = [avg_times[algo]['ATT'] for algo in algorithms]
    x = range(len(algorithms))
    plt.figure(figsize=(10, 6))
    plt.bar([i - 0.2 for i in x], awt_values, width=0.4, color='green', label='Average Waiting Time')
    plt.bar([i + 0.2 for i in x], att_values, width=0.4, color='purple', label='Average Turnaround Time')
    plt.xlabel('Scheduling Algorithms')
    plt.ylabel('Time (units)')
    plt.title('Comparison of Average Waiting and Turnaround Times')
    plt.xticks(x, algorithms)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
def plot_cpu_utilization(cpu_utils):
    import matplotlib.pyplot as plt
    algorithms = list(cpu_utils.keys())
    utilization_values = [cpu_utils[algo] for algo in algorithms]
    x = range(len(algorithms))
    plt.figure(figsize=(8, 5))
    plt.bar(x, utilization_values, color='skyblue')  # color: sky blue
    plt.xlabel('Scheduling Algorithms')
    plt.ylabel('CPU Utilization (%)')
    plt.title('CPU Utilization Comparison')
    plt.xticks(x, algorithms)
    plt.ylim(0, 100)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
def plot_throughput(throughputs):
    import matplotlib.pyplot as plt
    algorithms = list(throughputs.keys())
    throughput_values = [throughputs[algo] for algo in algorithms]
    x = range(len(algorithms))
    plt.figure(figsize=(8, 5))
    plt.bar(x, throughput_values, color='orange')  # color: orange
    plt.xlabel('Scheduling Algorithms')
    plt.ylabel('Throughput (processes/second)')
    plt.title('Throughput Comparison')
    plt.xticks(x, algorithms)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()