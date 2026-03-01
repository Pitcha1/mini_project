# disk.py

class DiskManager:

    def __init__(self):
        self.total_blocks = 50
        self.free = list(range(10, 50))
        self.files = {}
        self.mode = "contiguous"

    def init_disk(self, mode):
        self.mode = mode
        print(f"[INIT] Disk blocks=50 Allocation={mode.upper()}")
        print("Commands:")
        print("- create <file> <blocks>")
        print("- delete <file>")
        print("- ls")
        print("- map <file>")

    def create(self, name, size):

        start = self.free[0]
        blocks = list(range(start, start+size))

        for b in blocks:
            self.free.remove(b)

        self.files[name] = blocks

        print(f"[OK] Created {name} blocks={size} start={blocks[0]}..{blocks[-1]}")

    def delete(self, name):
        for b in self.files[name]:
            self.free.append(b)
        del self.files[name]
        print(f"[OK] Deleted {name}")

    def ls(self):
        print("FILES:")
        for name, blocks in self.files.items():
            print(f"- {name} contiguous [{blocks[0]}..{blocks[-1]}]")
        print("Free blocks:", len(self.free))

    def map(self, name):
        print(name, "->", " ".join(map(str, self.files[name])))