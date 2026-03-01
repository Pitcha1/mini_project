# memory.py

import math

class MemoryManager:

    def __init__(self):
        self.memory_size = 1024  # KB
        self.page_size = 4       # KB
        self.frames = self.memory_size // self.page_size
        self.page_tables = {}

    def init_memory(self):
        print(f"[INIT] Memory={self.memory_size}KB PageSize={self.page_size}KB Frames={self.frames}")

    def alloc(self, pid, kb):
        pages = math.ceil(kb/self.page_size)
        self.page_tables[pid] = list(range(pages))

        print(f"[OK] Alloc PID={pid} size={kb}KB => pages={pages}")
        for i in range(pages):
            print(f"VPN {i} -> PFN {i}")

    def translate(self, pid, logical_addr):
        page_size_bytes = self.page_size * 1024
        vpn = logical_addr // page_size_bytes
        offset = logical_addr % page_size_bytes
        pfn = self.page_tables[pid][vpn]
        physical = pfn * page_size_bytes + offset
        print("Physical Address =", physical)