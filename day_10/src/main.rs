use std::{collections::{HashMap, HashSet}, path, usize, vec};
// Trying a non type driven approach today


fn neighbours(loc: &(usize, usize)) -> Vec<(usize, usize)>{
    let (r, c) = loc.clone();

    let mut output = vec![(r + 1, c), (r, c + 1)];
    if r > 0{
        output.push((r - 1, c))
    }
    if c > 0 {
        output.push((r, c - 1));
    }

    return output;
}

fn increases_by_1(from: &u32, to: &u32) -> bool {
    to > from && (to - from) == 1
}

fn get_children(map: &HashMap<(usize, usize), u32>, loc: (usize, usize)) -> Vec<(usize, usize)> {
    let candidates = neighbours(&loc);
    candidates
    .iter()
    .filter(|location| {
        match map.get(&location) {
            Some(level) => increases_by_1(map.get(&loc).unwrap(), level),
            None => false,
        }
    })
    .map(Clone::clone)
    .collect()
}


fn traverse_hike(map: &HashMap<(usize, usize), u32>, frontier: &mut Vec<(usize, usize)>) -> HashSet<(usize, usize)>{
    let mut visited = HashSet::new();

    while let Some(loc) = frontier.pop() {
        visited.insert(loc);

        let children = get_children(map, loc);

        frontier.extend(children); // This is a finite graph so dfs suffices
        
    }

    visited
}


fn paths_between(map: &HashMap<(usize, usize), u32>, from: &(usize, usize), to: &(usize, usize)) -> Vec<Vec<(usize, usize)>> {
    if from == to {
        return vec![vec![]]
    }
    let children = get_children(map, from.clone());
    let next_steps = children
    .iter()
    .flat_map(|child| {
        paths_between(map, child, to)
        .iter()
        .map(|path| {
            let mut new = path.clone();
            new.push(from.clone());
            new
        })
        .collect::<Vec<_>>()
    })
    .collect::<Vec<_>>();

    next_steps    
}


fn main() {
    let input = include_str!("input.txt");

    let mut zeros = vec![];
    let mut map = HashMap::new();
    let mut nines = vec![];
    
    for (row, line) in input.lines().enumerate() {
        for (col, level) in line.char_indices() {
            if level == '0' {
                zeros.push((row, col));
            } else if level == '9' {
                nines.push((row, col));
            }
            map.insert((row, col), u32::try_from(u32::try_from(level).unwrap()).unwrap());
        }
    }


    let mut part1 = 0;
    let mut part2 = 0;
    for zero in zeros {
        let mut frontier = vec![zero.clone()];
        let visitable = traverse_hike(&map, &mut frontier);
        // let mut rating = 0;
        for nine in &nines {
            if visitable.contains(&nine) {
                part1 += 1;

                let paths = paths_between(&map, &zero, nine);
                // rating += paths.len();
                part2 += paths.len();

            }
        }
        // println!("{}", rating);

    }

    println!("Part 1: {part1}");
    println!("Part 2: {part2}");


}
