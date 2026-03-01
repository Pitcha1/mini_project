# process.py
# process.py

class PCB:
    def __init__(self, pid, arrival, burst, priority):
        self.pid = pid
        self.arrival_time = arrival
        self.burst_time = burst
        self.remaining_time = burst
        self.priority = priority

        self.state = "NEW"

        self.start_time = None
        self.finish_time = None
        self.waiting_time = 0
        self.turnaround_time = 0

    # reset สำหรับรันใหม่
    def reset(self):
        self.remaining_time = self.burst_time
        self.state = "NEW"
        self.start_time = None
        self.finish_time = None
        self.waiting_time = 0
        self.turnaround_time = 0


class ProcessManager:
    def __init__(self):
        self.processes = []

    # -----------------------------------
    # ADD PROCESS
    # -----------------------------------
    def add_process(self, pid, at, bt, pr):
        pcb = PCB(pid, at, bt, pr)
        self.processes.append(pcb)

        print(f"[OK] Added process: PID={pid} AT={at} BT={bt} PR={pr}")

        new_list = [p.pid for p in self.processes if p.state == "NEW"]
        print(f"ReadyQueue: (empty) | New: {new_list}")

    # -----------------------------------
    # LIST PROCESS
    # -----------------------------------
    def list_process(self):
        print("PID AT BT PR REM STATE")
        for p in self.processes:
            print(
                p.pid,
                p.arrival_time,
                p.burst_time,
                p.priority,
                p.remaining_time,
                p.state
            )

    # -----------------------------------
    # RESET ALL (ก่อนรัน scheduler ใหม่)
    # -----------------------------------
    def reset_all(self):
        for p in self.processes:
            p.reset()