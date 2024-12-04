import re

from functools import partial
from itertools import product, chain


def safe_access(list, index):
    return list[index] if index >= 0 and index < len(list) else None


class XmasWordSearch:

    def __init__(self, search):
        lines = search.strip().split("\n")
        self.board = [l.strip() for l in lines]

    def x_coords(self):
        return ((row, match.start()) for row, line in enumerate(self.board)
                for match in re.finditer("X", line))

    def __getitem__(self, coord):
        row, col = coord
        line = safe_access(self.board, row)
        return safe_access(line, col) if line is not None else None

    def find_ms(self, x):
        r, c = x

        def conditions(coord):
            return coord != x and self[coord] == "M"

        return [coord for coord in product([r - 1, r, r + 1], [c - 1, c, c + 1]) if conditions(coord)]

    @staticmethod
    def expand_xmas(x, m):
        r1, c1 = x
        r2, c2 = m

        r_diff = r2 - r1
        c_diff = c2 - c1

        a = r2 + r_diff, c2 + c_diff
        s = r2 + 2 * r_diff, c2 + 2 * c_diff

        return x, m, a, s

    def is_valid_xmas(self, xmas):
        xmas_letters = [self[letter] for letter in xmas]
        return xmas_letters == ['X', 'M', 'A', 'S']

    def find_xmas_coords(self):
        xs = self.x_coords()

        starts = chain(*[[(x, m) for m in self.find_ms(x)] for x in xs])

        candidates = (self.expand_xmas(*start) for start in starts)
        return [xmas for xmas in candidates if self.is_valid_xmas(xmas)]

    def count_xmases(self):
        return len(self.find_xmas_coords())

    def __repr__(self):
        return "\n".join(self.board)

    def display_subset(self, subset):
        return "\n".join(
            "".join(
                char if (row, col) in subset else "." for col, char in enumerate(line))
            for row, line in enumerate(self.board))

    def display_soln(self):
        coords = set(chain(*self.find_xmas_coords()))
        return self.display_subset(coords)


class XMasWordSearch:
    """
    That'll teach me to switch to a more involved approach to preempt part 2.

    I'm not subclassing because the classes are *just* different enough that I'd consider that a footgun.
    If this were a project I'd abstact away common elements, though.
    """

    def __init__(self, search):
        lines = search.strip().split("\n")
        self.board = [l.strip() for l in lines]

    def a_coords(self):
        return ((row, match.start()) for row, line in enumerate(self.board)
                for match in re.finditer("A", line))

    def __getitem__(self, coord):
        row, col = coord
        line = safe_access(self.board, row)
        return safe_access(line, col) if line is not None else None

    def find_ms(self, a):
        r, c = a
        candidates = [(r - 1, c - 1), (r - 1, c + 1),
                      (r + 1, c - 1), (r + 1, c + 1)]
        return [coord for coord in candidates if self[coord] == "M"]

    @staticmethod
    def continue_line(x1, x2):
        r1, c1 = x1
        r2, c2 = x2

        r_diff = r2 - r1
        c_diff = c2 - c1

        return r2 + r_diff, c2 + c_diff

    def expand_x_mas(self, triplet):
        m1, m2, a = triplet

        s1 = self.continue_line(m1, a)
        s2 = self.continue_line(m2, a)
        if self[s1] != "S" or self[s2] != "S":

            return None
        else:
            return [m1, s1, a, m2, s2]

    def get_x_masses(self):
        centres = self.a_coords()
        # This doesn't remove the case where the three letters are aligned, instead of v shaped,
        # but it's an easy first cull.
        triplets = filter(lambda l: len(l) == 3,
                          (self.find_ms(a) + [a] for a in centres))

        return [x for x in map(self.expand_x_mas, triplets) if x != None]

    def count_x_masses(self):
        return len(self.get_x_masses())

    def __repr__(self):
        return "\n".join(self.board)

    def display_subset(self, subset):
        return "\n".join(
            "".join(
                char if (row, col) in subset else "." for col, char in enumerate(line))
            for row, line in enumerate(self.board))

    def display_soln(self):
        coords = set(chain(*self.get_x_masses()))
        return self.display_subset(coords)


def main():
    search = """
    MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX
    """

    board = XmasWordSearch(search)
    print(f"Part 1: {board.count_xmases()}")

    new_board = XMasWordSearch(search)
    print(f"Part 2: {new_board.count_x_masses()}")


if __name__ == "__main__":
    main()
