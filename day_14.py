from collections import Counter
from functools import reduce
import re

WIDTH = 101
HEIGHT = 103


def parse_robot(robot):
    regex = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"

    numbers = re.search(regex, robot)

    return (
        (int(numbers.group(1)), int(numbers.group(2))),
        (int(numbers.group(3)), int(numbers.group(4))),
    )


def move_location(robot, num_steps):
    (x0, y0), (vx, vy) = robot

    x = (x0 + vx * num_steps) % WIDTH
    y = (y0 + vy * num_steps) % HEIGHT

    return x, y


def count_in_quadrants(robots):
    pillar = (WIDTH) // 2
    beam = (HEIGHT) // 2
    ul = [(x, y) for x, y in robots if y < beam and x < pillar]
    ur = [(x, y) for x, y in robots if y < beam and x > pillar]
    ll = [(x, y) for x, y in robots if y > beam and x < pillar]
    lr = [(x, y) for x, y in robots if y > beam and x > pillar]
    return reduce(lambda a, b: a * b, (len(quad) for quad in [ul, ur, ll, lr]))


def main():
    inpt = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
""".strip()

    robots = [parse_robot(robot) for robot in inpt.splitlines()]

    # robots = [((2, 4), (2, -3))]
    ending_locations = [move_location(robot, 100) for robot in robots]
    # print(ending_locations)
    # display_robots(ending_locations)
    # print("---")
    part1 = count_in_quadrants(ending_locations)

    print(part1)

    print("---")

    # part 2 is some nonsense.
    boards = [(i, [move_location(robot, i) for robot in robots])
              for i in range(10_000)]
    sorted_boards = sorted(
        boards, key=lambda board: count_in_quadrants(board[1]))

    for i, board in sorted_boards:
        print(i)
        display_robots(board)
        input()


def display_robots(robots):
    robot_freqs = Counter(robots)
    board = []
    for col in range(HEIGHT):
        bar = []
        for row in range(WIDTH):
            bar.append(str(robot_freqs[(row, col)] or "."))
        board.append("".join(bar))
    print("\n".join(board))


if __name__ == "__main__":
    main()
