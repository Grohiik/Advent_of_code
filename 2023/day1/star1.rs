fn main() {
    let my_str = include_str!("input.txt").split("\n").collect::<Vec<_>>();
    let mut out = 0;

    for row in my_str {
        let mut temp = Vec::new();
        for char in row.chars() {
            if char.is_ascii_digit() {
                temp.push(char);
            }
        }
        if temp.len() > 0 {
            let mut blub = String::from("");
            blub.push(temp[0]);
            blub.push(temp.last().copied().expect(""));

            out += blub.parse::<i32>().unwrap();
        }
    }
    print!("{out}");
}
