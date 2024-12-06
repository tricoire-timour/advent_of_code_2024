use std::{collections::HashSet, num::ParseIntError};

struct RuleBook(Vec<OrderingRule>);

#[derive(Debug, Clone, Copy)]
struct OrderingRule(u32, u32);

impl TryFrom<&str> for OrderingRule {
    type Error = color_eyre::Report;

    fn try_from(value: &str) -> Result<Self, Self::Error> {
        let numbers: Vec<u32> = value
            .split("|")
            .map(&str::parse::<u32>)
            .collect::<Result<Vec<u32>, ParseIntError>>()?;

        // Necessarily, numbers.len == 2.
        Ok(OrderingRule(numbers[0], numbers[1]))
    }
}

impl TryFrom<&str> for RuleBook {
    type Error = color_eyre::Report;

    fn try_from(value: &str) -> Result<Self, Self::Error> {
        let inner = value
            .lines()
            .map(OrderingRule::try_from)
            .filter(Result::is_ok)
            .map(Result::unwrap)
            .collect::<Vec<OrderingRule>>();

        Ok(Self(inner))
    }
}

impl OrderingRule {
    fn get_relevant_positions(&self, page_list: &Vec<u32>) -> Option<(usize, usize)> {
        let first_posn = page_list.iter().position(|i| i == &self.0)?;
        let second_posn = page_list.iter().position(|i| i == &self.1)?;

        Some((first_posn, second_posn))
    }

    fn applies(&self, page_list: &Vec<u32>) -> bool {
        match self.get_relevant_positions(page_list) {
            None => true,
            Some((l, r)) => l < r,
        }
    }
}

impl RuleBook {
    fn applies(&self, page_list: &Vec<u32>) -> bool {
        self.0.iter().all(|rule| rule.applies(page_list))
    }

    fn order(&self, page_list: &Vec<u32>) -> Vec<u32> {
        if page_list.len() <= 1 {
            return page_list.clone();
        }
        let relevant_rules = self
            .0
            .iter()
            .filter(|rule| rule.get_relevant_positions(page_list).is_some())
            .collect::<Vec<_>>();

        let lefts = relevant_rules.iter().map(|r| r.0).collect::<HashSet<_>>();
        let rights = relevant_rules.iter().map(|r| r.1).collect::<HashSet<_>>();
        let pure_rights = &rights - &lefts;
        if pure_rights.len() > 1 {
            println!("New example!");
            println!("{:?}", page_list);
            for rule in relevant_rules {
                println!("{}|{}", rule.0, rule.1)
            }
            panic!("The unreasonable assumption I made was in fact unreasonable")
        }
        let rightmost = pure_rights.iter().next().unwrap(); // If there's no pure lefts, then we are done for.

        let others = page_list
            .iter()
            .filter(|i| i != &rightmost)
            .map(Clone::clone)
            .collect::<Vec<_>>();

        let rest = Self(relevant_rules.iter().map(|inpt| (*inpt).clone()).collect());

        let mut ordered = rest.order(&others);
        ordered.push(rightmost.clone());
        ordered
    }
}

fn main() -> color_eyre::Result<()> {
    let input = include_str!("input.txt");

    let rules_then_pagelist = input.split("\n\n").collect::<Vec<_>>();

    let rules: RuleBook = rules_then_pagelist[0].try_into()?;

    let pagelists = rules_then_pagelist[1]
        .lines()
        .map(|list| {
            list.split(",")
                .map(&str::parse::<u32>)
                .collect::<Result<Vec<u32>, ParseIntError>>()
        })
        .collect::<Result<Vec<_>, ParseIntError>>()?;

    let part_1: u32 = pagelists
        .iter()
        .filter(|pages| rules.applies(pages))
        .map(|l| l[l.len() / 2])
        .sum();

    println!("Part 1: {part_1}");

    let part_2: u32 = pagelists
        .iter()
        .filter(|pages| !rules.applies(pages))
        .map(|page| rules.order(page))
        .map(|l| l[l.len() / 2])
        .sum();

    println!("Part 2: {part_2}");

    Ok(())
}
