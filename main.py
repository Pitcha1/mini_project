# main.py

from scheduler import Scheduler
from paging import simulate_page
from disk import DiskManager
from process import ProcessManager


def main():
    pm = ProcessManager()
    scheduler = Scheduler(pm)
    disk = DiskManager()

    print("===== OS Simulator =====")

    while True:
        cmd = input("os-sim> ").strip().split()
        if not cmd:
            continue

        # -------------------------
        # EXIT
        # -------------------------
        if cmd[0] == "exit":
            break

        # -------------------------
        # PROCESS
        # -------------------------
        elif cmd[0] == "add_process":
            pm.add_process(
                int(cmd[1]), int(cmd[2]),
                int(cmd[3]), int(cmd[4])
            )

        elif cmd[0] == "list_process":
            pm.list_process()

        elif cmd[0] == "run_scheduler":
            alg = cmd[1].upper()

            if alg == "FCFS":
                scheduler.run_fcfs()
            elif alg == "SJF":
                scheduler.run_sjf()
            elif alg == "RR":
                scheduler.run_rr(int(cmd[2]))

        elif cmd[0] == "show_gantt":
            scheduler.show_gantt()

        elif cmd[0] == "show_table":
            scheduler.show_table()

        # -------------------------
        # PAGING
        # -------------------------
        elif cmd[0] == "simulate_memory" and cmd[1] == "paging":
            print("[INIT] Memory=1024KB  PageSize=4KB  Frames=256")
            print("[OK] Paging enabled (simulation)")
            print("\nCommands:")
            print("- alloc <pid> <kb>")
            print("- translate <pid> <logical_addr>")
            print("- free <pid>")

        # -------------------------
        # DISK
        # -------------------------
        elif cmd[0] == "simulate_disk":
            disk.init_disk(cmd[1])

        elif cmd[0] == "create":
            disk.create(cmd[1], int(cmd[2]))

        elif cmd[0] == "delete":
            disk.delete(cmd[1])

        elif cmd[0] == "ls":
            disk.ls()

        elif cmd[0] == "map":
            disk.map(cmd[1])


if __name__ == "__main__":
    main()