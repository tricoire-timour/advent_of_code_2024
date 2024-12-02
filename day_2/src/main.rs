use std::num::ParseIntError;

/// Represents a line of data from the Red-Nosed Reactor
struct Report(Vec<u32>);

impl TryFrom<&str> for Report {
    type Error = ParseIntError;

    fn try_from(value: &str) -> Result<Self, Self::Error> {
        value.split(' ')
        .map(|i| {
            i
            .parse::<u32>()
        })
        .collect::<Result<Vec<u32>, _>>()
        .map(|v| {Report(v)})
    }
}

/// Returns list with the idxth element skipped
fn skip<A>(list: &Vec<A>, idx: &usize) -> Vec<A> where A: Clone {
    // If this were a bigger project I'd define a custom iterator but
    
    list
    .iter()
    .enumerate()
    .filter(|(i, _)| {i != idx})
    .map(|(_, v)| v.clone())
    .collect()
}

impl Report {
    /// Reverses the inner list of the report
    fn reverse(&self) -> Self {
        Self(self.0.iter().rev().map(|i|{i.clone()}).collect())
    }

    /// Checks whether the report is sorted
    fn is_sorted(&self) -> bool {
        self.0.is_sorted()
    }

    /**  
     * Checks if, for an ascending report, every adjacent pair has an increase of at least 1 and at most 3 
     */
    fn proper_increases(&self) -> bool {
        self.0.windows(2).all(|pair| {
            assert!(pair.len() == 2);
            let diff = pair[1] - pair[0];
            (1..=3).contains(&diff)
        })
    }

    fn is_safe(&self) -> bool {
        self.is_sorted() && self.proper_increases() 
        || self.reverse().is_sorted() && self.reverse().proper_increases()
    }

    fn test_removals(&self) -> Vec<Self> {
        (0..self.0.len())
        .map(|idx| {
            Self(skip(&self.0, &idx))
        })
        .collect()
    }

    fn dampened_safe(&self) -> bool {
        self.is_safe() || self.test_removals().iter().any(Report::is_safe)
    }
}

fn main() -> Result<(), ParseIntError> {
    let inpt = include_str!("./input.txt");

    let safe_reports = inpt.lines().filter(|&report_str | {
        Report::try_from(report_str)
        .expect(&format!("The line \"{report_str}\" is not a valid report"))
        .is_safe()
    })
    .count();

    println!("Part 1: {safe_reports} reports are safe");

    println!("Activating problem dampener...");
    
    let dampened_safe_reports = inpt.lines().filter(|&report_str | {
        Report::try_from(report_str)
        .expect(&format!("The line \"{report_str}\" is not a valid report"))
        .dampened_safe()
    })
    .count();

    println!("Part 2: {dampened_safe_reports} reports are safe");

    Ok(())
}
