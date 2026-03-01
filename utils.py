# utils.py

def show_gantt(gantt):
    print("Gantt Chart:")
    for start, end, pid in gantt:
        print(f"[{start:2}..{end:2}] P{pid}", end=" ")
    print()
    