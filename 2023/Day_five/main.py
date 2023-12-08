from collections import defaultdict

D = open("input.txt", "r").read().strip()
L = D.split('\n')

parts = D.split('\n\n')
seed, *others = parts
seed = [int(x) for x in seed.split(':')[1].split()]

class Garden:
    def __init__(self, S):
        lines = S.split('\n')[1:]  # throw away name
        # Create a tuple of data from "other"
        self.tuples: list[tuple[int, int, int]] = [[int(x) for x in line.split()] for line in lines]

    def apply_one(self, x: int) -> int:
        print(x)
        for (dst, src, rl) in self.tuples:
            if src <= x < src + rl:
                return x + dst - src
        return x

    # list of [start, end) ranges
    def apply_range(self, R):
        A = []
        for (dest, src, rl) in self.tuples:
            src_end = src + rl
            NR = []
            while R:
                (st, ed) = R.pop()
                before = (st, min(ed, src))
                inter = (max(st, src), min(src_end, ed))
                after = (max(src_end, st), ed)
                if before[1] > before[0]:
                    NR.append(before)
                if inter[1] > inter[0]:
                    A.append((inter[0] - src + dest, inter[1] - src + dest))
                if after[1] > after[0]:
                    NR.append(after)
            R = NR
        return A + R


garden_info = [Garden(s) for s in others]

def part_one():
    P1 = []
    for x in seed:
        print(x)
        for f in garden_info:
            x = f.apply_one(x)
        P1.append(x)
    print(min(P1))


def part_two():
    P2 = []
    pairs = list(zip(seed[::2], seed[1::2]))
    for st, sz in pairs:
        R = [(st, st + sz)]
        for f in garden_info:
            R = f.apply_range(R)
        P2.append(min(R)[0])
    print(min(P2))


if __name__ == "__main__":
    part_one()
    # part_two()
