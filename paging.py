# paging.py

def simulate_page(alg, frames, ref):

    print(f"[RUN] PageReplacement={alg} Frames={frames}")
    print("Ref | Frames | Result")

    memory = []
    faults = 0
    hits = 0

    for i, page in enumerate(ref):

        if page in memory:
            hits += 1
            print(f"{page} | {memory} | HIT")
            continue

        faults += 1

        if len(memory) < frames:
            memory.append(page)
            print(f"{page} | {memory} | FAULT")
        else:

            if alg == "FIFO":
                evicted = memory.pop(0)

            elif alg == "LRU":
                future = ref[:i]
                lru = min(memory, key=lambda x: future[::-1].index(x))
                evicted = lru
                memory.remove(lru)

            elif alg == "OPTIMAL":
                future = ref[i+1:]
                farthest = -1
                evicted = None
                for m in memory:
                    if m not in future:
                        evicted = m
                        break
                    idx = future.index(m)
                    if idx > farthest:
                        farthest = idx
                        evicted = m
                memory.remove(evicted)

            memory.append(page)
            print(f"{page} | {memory} | FAULT (evict {evicted})")

    print("Summary:")
    print(f"- Page Faults = {faults}")
    print(f"- Hits = {hits}")
    ratio = (hits/(hits+faults))*100 if (hits+faults)>0 else 0
    print(f"- Hit Ratio = {ratio:.2f}%")