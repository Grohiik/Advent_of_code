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
            .for_each(|ball: Vec<&str>| {
                out.entry(ball[1])
                    .and_modify(|num| *num = cmp::max(*num, ball[0].parse::<i32>().unwrap()));
            })
    });

    return out;
}

fn main() {
    let awnser: i32 = include_str!("input.txt")
        .lines()
        .map(|line| line.split(':').collect::<Vec<&str>>()[1])
        .map(|game| {
            let cubehash = cubesum(game);
            return cubehash.get("red").unwrap()
                * cubehash.get("green").unwrap()
                * cubehash.get("blue").unwrap();
        })
        .sum();
    println!("{awnser}")
}
