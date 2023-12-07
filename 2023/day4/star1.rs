fn numsum(winning: Vec<&str>, mine: Vec<&str>) -> u32 {
    let mut out = 0;

    for win in &winning {
        for num in &mine {
            if (&win).eq(&num) {
                out += 1;
            }
        }
    }
    out
}

fn main() {
    let awnser: i32 = include_str!("input.txt")
        .lines()
        .map(|game| {
            let mut game_iter = game.split(&[':', '|']).skip(1).map(|numheep| {
                numheep
                    .split(' ')
                    .filter(|p| !p.is_empty())
                    .collect::<Vec<&str>>()
            });
            let numsum = numsum(game_iter.next().unwrap(), game_iter.next().unwrap());
            if numsum > 0 {
                2_i32.pow(numsum - 1)
            } else {
                0
            }
        })
        .sum();
    println!("{}", awnser);
}
