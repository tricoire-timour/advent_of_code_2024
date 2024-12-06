import copy
from functools import partial
from itertools import chain


def parse_map(input):
    pillars = []
    dots = []
    for row, line in enumerate(input.splitlines()):
        for col, character in enumerate(line.strip()):
            match character:
                case ".":
                    dots.append((row, col))
                case "#":
                    pillars.append((row, col))
                case "^":
                    guard = ((row, col), "^")
                case other:
                    print(f"found other character '{other}'")

    return pillars, guard, row, col, dots


def next_pillar(guard, pillars):
    (guard_r, guard_c), guard_dir = guard
    cross = [(r, c) for r, c in pillars if r == guard_r or c == guard_c]

    match guard_dir:
        case "^":
            pillars = [(row, col) for row, col in cross if row < guard_r]
        case ">":
            pillars = [(row, col) for row, col in cross if col > guard_c]
        case "v":
            pillars = [(row, col) for row, col in cross if row > guard_r]
        case "<":
            pillars = [(row, col) for row, col in cross if col < guard_c]

    return min(pillars, key=partial(manhattan, (guard_r, guard_c))) if len(pillars) != 0 else None


def just_shy(dir, coord):
    (r, c) = coord
    match dir:
        case "^":
            return (r + 1, c)
        case ">":
            return (r, c - 1)
        case "v":
            return (r - 1, c)
        case "<":
            return (r, c + 1)


def next_dir(dir):
    match dir:
        case "^":
            return ">"
        case ">":
            return "v"
        case "v":
            return "<"
        case "<":
            return "^"


def distance_left(guard, bottom, right):
    coord, dir = guard
    match dir:
        case "^":
            return coord[0]
        case ">":
            return right - coord[1]
        case "v":
            return bottom - coord[0]
        case "<":
            return coord[1]


def manhattan(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


# def distances(dists):
#     dist = 0
#     for pair in zip(dists, dists[1:]):
#         dist += manhattan(*pair)
#     return dist


def endpoint(guard, bottom, right):
    (r, c), dir = guard
    match dir:
        case "^":
            return (0, c)
        case ">":
            return (r, right)
        case "v":
            return (bottom, c)
        case "<":
            return (r, 0)


def myrange(p1, p2):
    if p1 > p2:
        return range(p2, p1 + 1)
    else:
        return range(p1, p2 + 1)


def interpolate(van, naar):
    r1, c1 = van
    r2, c2 = naar

    run = myrange(c1, c2)
    rise = myrange(r1, r2)

    vertical = [(r, c1) for r in rise]
    across = [(r2, c) for c in run]
    return chain(vertical, across)


def fill_out(turning_points):
    acc = []
    for pair in zip(turning_points, turning_points[1:]):
        acc = chain(acc, interpolate(*pair))
    return set(acc)


def do_part_1(pillars, guard, max_row, max_col):
    turning_points = [guard[0]]
    obstacle = next_pillar(guard, pillars)
    while obstacle is not None:
        tp = just_shy(guard[1], obstacle)
        if tp in turning_points[:-1]:
            return None
        new_dir = next_dir(guard[1])
        turning_points.append(tp)
        guard = (tp, new_dir)
        obstacle = next_pillar(guard, pillars)
    capped = turning_points + [endpoint(guard, max_row, max_col)]
    trodden = fill_out(capped)
    return len(trodden), turning_points


def brute_force(input, dots):
    """
    I don't want to do this but it's wind and truth release day and my friend 
    who's a better programmer than me did it too.
    """

    spot_count = 0
    for r, c in dots:
        new_in = "\n".join(["".join(["#" if (row, col) == (r, c) else char for col, char in enumerate(
            line.strip())]) for row, line in enumerate(input.splitlines())])
        pillars, guard, max_row, max_col, _ = parse_map(new_in)
        if do_part_1(pillars, guard, max_row, max_col) is None:
            spot_count += 1
            print(spot_count)
    return spot_count


def main():
    input: str = """
    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#..^.....
    ........#.
    #.........
    ......#...
    """.strip()

    pillars, guard, max_row, max_col, dots = parse_map(input)

    part_1, turning_points = do_part_1(pillars, guard, max_row, max_col)

    print(f"part 1: {part_1}")

    part_2 = brute_force(input, dots)
    print(f"part 2: {part_2}")


if __name__ == "__main__":
    main()
