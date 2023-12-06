use std::cmp;
use std::collections::HashMap;

// Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

fn cubesum(string_input: &str) -> HashMap<&str, i32> {
    let mut out = HashMap::new();
    out.insert("red", 0);
    out.insert("green", 0);
    out.insert("blue", 0);

    string_input.split(';').for_each(|round| {
        round
            .split([','])
            .map(|x| x.split(' ').filter(|p| !p.is_empty()).collect())
            .for_each(|cube: Vec<&str>| {
                out.entry(cube[1])
                    .and_modify(|num| *num = cmp::max(*num, cube[0].parse::<i32>().unwrap()));
            })
    });

    return out;
}

fn main() {
    let awnser: i32 = include_str!("input.txt")
        .lines()
        .map(|line| line.split(':').collect())
        .filter(|line: &Vec<&str>| {
            let cubehash = cubesum(line[1]);
            return cubehash.get("red").unwrap() <= &i32::from(12)
                && cubehash.get("green").unwrap() <= &i32::from(13)
                && cubehash.get("blue").unwrap() <= &i32::from(14);
        })
        .map(|line| {
            line[0].split(' ').collect::<Vec<&str>>()[1]
                .parse::<i32>()
                .unwrap()
        })
        .sum();
    println!("{awnser}")
}
