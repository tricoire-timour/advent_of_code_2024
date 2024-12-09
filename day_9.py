

from copy import copy


def first_empty(mem):
    end_of_previous_block = 0
    for list_id, (_, start_index, length) in enumerate(mem):
        if start_index > end_of_previous_block:
            return list_id, end_of_previous_block
        else:
            end_of_previous_block += length


def has_gaps(mem):
    index = 0
    for _, start, length in mem:
        if index != start:
            return True
        else:
            index += length


def dbg(thing):
    print(thing)
    return thing


def shift_left(mem):
    list_ind, first_empty_index = first_empty(mem)
    id, last_start, last_length = mem[-1]

    # remove last element
    if last_length == 1:
        mem.pop()
    else:
        mem[-1] = (id, last_start, last_length - 1)

    # put it in the first empty slot
    if (existing := mem[list_ind - 1])[0] == id:
        mem[list_ind - 1] = (id, existing[1], existing[2] + 1)
    else:
        mem.insert(list_ind, (id, first_empty_index, 1))


def gap_info(mem):
    end_of_previous_block = 0
    for list_ind, (_, start_index, length) in enumerate(mem):
        if end_of_previous_block != start_index:
            return end_of_previous_block, start_index - end_of_previous_block, list_ind
        end_of_previous_block += length


def fill_gap(mem):
    gap_index, gap_length, list_index = gap_info(mem)
    id, last_start, last_length = mem[-1]

    # remove a chunk from the end
    if last_length > gap_length:
        mem[-1] = (id, last_start, last_length - gap_length)
    else:
        mem.pop()

    # add the chunk to the start
    mem.insert(list_index, (id, gap_index, min(last_length, gap_length)))


def compute_checksum(mem):
    return sum([posn * int(id) for posn, id in enumerate(list_block(mem)) if id is not None])


def list_block(mem):
    output = []
    prev_index = 0
    for id, start_index, length in mem:
        output.extend((start_index - prev_index) * [None])
        output.extend([id] * length)
        prev_index = start_index + length
    return output


def display_block(mem):
    """
    Only works for small inputs
    """
    return "".join([str(id) if id is not None else "." for id in list_block(mem)])


def do_part_1(mem):
    while has_gaps(mem):
        fill_gap(mem)
    return compute_checksum(mem)


def mem_to_map(mem):
    return {id: (block_start, block_length) for id, block_start, block_length in mem}


def mem_to_list(mem):
    jumbled = [(id, block_start, block_length)
               for (id, (block_start, block_length)) in mem.items()]
    jumbled.sort(key=lambda i: i[1])
    return jumbled


def get_gaps(mem):
    gaps = []
    previous_end = mem[0][2]
    for _, start, length in mem:
        if start != previous_end:
            gaps.append((previous_end, start))
        previous_end = start + length
    return gaps


def find_gap(memory, length, limit):
    mem = mem_to_list(memory)

    gaps = get_gaps(mem)
    valid_gaps = [(start, end) for start, end in gaps if (
        end - start) >= length and end <= limit]
    return valid_gaps[0] if len(valid_gaps) != 0 else None


def try_move_left(mem, id):
    start, length = mem[id]
    gap = find_gap(mem, length, start)
    if gap is not None:
        start, _ = gap
        mem[id] = (start, length)


def do_part_2(mem, max_id):
    display_block(mem)
    mem = mem_to_map(mem)
    for id in reversed(range(max_id + 1)):
        try_move_left(mem, id)
        # displ = mem_to_list(mem)
        # print(display_block(displ))
    mem = mem_to_list(mem)
    return compute_checksum(mem)


def main():
    input = "2333133121414131402"
    mem = []
    index = 0
    for twice_id, block in enumerate(input):
        block = int(block)
        if twice_id % 2 == 0:
            mem.append((twice_id//2, index, block))
        index += block

    max_id = twice_id // 2

    part1 = do_part_1(copy(mem))
    print(f"Part 1: {part1}")

    part2 = do_part_2(mem, max_id)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
