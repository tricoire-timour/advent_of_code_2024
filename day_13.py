import re
from typing import Dict


def parse_claw_machine(machinestring: str, part2: bool = False) -> Dict[str, int]:
    regex_A = r"Button A: X\+(\d+), Y\+(\d+)"
    regex_B = r"Button B: X\+(\d+), Y\+(\d+)"
    regex_S = r"Prize: X=(\d+), Y=(\d+)"
    # print(regex_A)
    a_search = re.search(regex_A, machinestring)
    b_search = re.search(regex_B, machinestring)
    s_search = re.search(regex_S, machinestring)

    return {
        "ax": int(a_search.group(1)),
        "ay": int(a_search.group(2)),
        "bx": int(b_search.group(1)),
        "by": int(b_search.group(2)),
        "sx": int(s_search.group(1)) + 10000000000000 * part2,
        "sy": int(s_search.group(2)) + 10000000000000 * part2,
    }


def solve_machine(ax: int, ay: int, bx: int, by: int, sx: int, sy: int):
    det = 1 / (ax * by - bx * ay)
    a = det * (by * sx - bx * sy)
    b = det * (ax * sy - ay * sx)

    return a, b



def main():
    input: str = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
    """.strip()

    PART_2 = True

    machines = [parse_claw_machine(machine, PART_2) for machine in input.split("\n\n")]
    print(machines[0])

    print(solve_machine(**machines[0]))
    attempts = [solve_machine(**machine) for machine in machines]

    costs = [3 * round(a) + round(b) for a, b in attempts if is_reasonable_int(a) and is_reasonable_int(b)]
    
    tokens = sum(costs)

    print(tokens)


def is_reasonable_int(n):
    return abs(n - round(n)) < 0.01


if __name__ == "__main__":
    main()