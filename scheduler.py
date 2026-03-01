class PCB:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.state = "NEW"
        self.start_time = None
        self.finish_time = None


class Scheduler:

    def __init__(self, process_manager):
        self.pm = process_manager
        self.gantt = []

    # --------------------------------
    # FCFS
    # --------------------------------
    def run_fcfs(self):
        print("[RUN] Scheduler=FCFS")
        self._reset_processes()

        time = 0
        ready = []
        self.gantt = []

        procs = sorted(self.pm.processes, key=lambda x: x.arrival_time)

        while any(p.state != "TERMINATED" for p in procs):

            for p in procs:
                if p.arrival_time <= time and p.state == "NEW":
                    p.state = "READY"
                    ready.append(p)
                    print(f"[TIME {time}] Arrivals: P{p.pid} -> READY")

            if ready:
                p = ready.pop(0)
                p.state = "RUNNING"
                p.start_time = time
                print(f"[TIME {time}] Dispatch: P{p.pid}")

                time += p.burst_time
                p.finish_time = time
                p.state = "TERMINATED"
                print(f"[TIME {time}] P{p.pid} finished")

                self.gantt.append((p.start_time, p.finish_time, p.pid))
            else:
                time += 1

        print(f"[DONE] All processes terminated at time={time}")
        self.print_metrics()

    # --------------------------------
    # SJF (Non-preemptive)
    # --------------------------------
    def run_sjf(self):
        print("[RUN] Scheduler=SJF (non-preemptive)")
        self._reset_processes()

        time = 0
        ready = []
        self.gantt = []

        procs = sorted(self.pm.processes, key=lambda x: x.arrival_time)

        while any(p.state != "TERMINATED" for p in procs):

            for p in procs:
                if p.arrival_time <= time and p.state == "NEW":
                    p.state = "READY"
                    ready.append(p)
                    print(f"[TIME {time}] Arrivals: P{p.pid} -> READY")

            if ready:
                ready.sort(key=lambda x: x.burst_time)
                p = ready.pop(0)

                p.state = "RUNNING"
                p.start_time = time
                print(f"[TIME {time}] Dispatch: P{p.pid} (BT={p.burst_time})")

                time += p.burst_time
                p.finish_time = time
                p.state = "TERMINATED"
                print(f"[TIME {time}] P{p.pid} finished")

                self.gantt.append((p.start_time, p.finish_time, p.pid))
            else:
                time += 1

        print(f"[DONE] All processes terminated at time={time}")
        self.print_metrics()

    # --------------------------------
    # RR
    # --------------------------------
    def run_rr(self, q):
        print(f"[RUN] Scheduler=RR q={q}")
        self._reset_processes()

        time = 0
        ready = []
        self.gantt = []

        procs = sorted(self.pm.processes, key=lambda x: x.arrival_time)

        while any(p.state != "TERMINATED" for p in procs):

            for p in procs:
                if p.arrival_time <= time and p.state == "NEW":
                    p.state = "READY"
                    ready.append(p)
                    print(f"[TIME {time}] Arrivals: P{p.pid} -> READY")

            if ready:
                p = ready.pop(0)

                if p.start_time is None:
                    p.start_time = time

                run_time = min(q, p.remaining_time)
                print(f"[TIME {time}] Dispatch: P{p.pid} (run {run_time})")

                start = time
                time += run_time
                p.remaining_time -= run_time

                self.gantt.append((start, time, p.pid))

                if p.remaining_time == 0:
                    p.finish_time = time
                    p.state = "TERMINATED"
                    print(f"[TIME {time}] P{p.pid} finished")
                else:
                    print(f"[TIME {time}] Preempt: P{p.pid} REM={p.remaining_time} -> READY")
                    ready.append(p)
            else:
                time += 1

        print(f"[DONE] All processes terminated at time={time}")
        self.print_metrics()

    # --------------------------------
    def show_gantt(self):
        print("Gantt Chart:")
        for s, e, pid in self.gantt:
            print(f"[{s:2}..{e:2}] P{pid}", end=" ")
        print()

    # --------------------------------
    def show_table(self):
        print("PID AT BT ST FT WT TAT")
        for p in self.pm.processes:
            wt = p.finish_time - p.arrival_time - p.burst_time
            tat = p.finish_time - p.arrival_time

            print(
                p.pid,
                p.arrival_time,
                p.burst_time,
                p.start_time,
                p.finish_time,
                wt,
                tat
            )

    # --------------------------------
    def print_metrics(self):
        total_wt = 0
        total_tat = 0

        for p in self.pm.processes:
            wt = p.finish_time - p.arrival_time - p.burst_time
            tat = p.finish_time - p.arrival_time

            total_wt += wt
            total_tat += tat

        n = len(self.pm.processes)

        print("Metrics:")
        print(f"- Avg Waiting Time = {total_wt/n:.2f}")
        print(f"- Avg Turnaround Time = {total_tat/n:.2f}")

    # --------------------------------
    def _reset_processes(self):
        for p in self.pm.processes:
            p.state = "NEW"
            p.remaining_time = p.burst_time
            p.start_time = None
            p.finish_time = None