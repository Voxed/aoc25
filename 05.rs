use std::cmp;
use std::error::Error;
use std::io::{self, Read};

fn main() -> Result<(), Box<dyn Error>> {
    let mut input: String = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    input = input.replace("\r\n", "\n");

    let (ranges, ingredients) = input.split_once("\n\n").unwrap();

    let mut ranges = ranges
        .split('\n')
        .map(|s| -> Result<_, Box<dyn Error>> {
            let (a, b) = s.split_once('-').ok_or("Invalid range format")?;
            Ok((a.parse::<u64>()?, b.parse::<u64>()? + 1))
        })
        .collect::<Result<Vec<_>, _>>()?;
    ranges.sort();

    let ingredients = ingredients
        .split('\n')
        .filter(|i| !i.is_empty())
        .map(str::parse::<u64>)
        .collect::<Result<Vec<_>, _>>()?;

    println!(
        "{}",
        ingredients
            .iter()
            .filter(|&i| ranges.iter().any(|(start, end)| start < i && i <= end))
            .count()
    );

    let (mut cursor, mut sum) = (0u64, 0u64);
    for (start, end) in ranges {
        if cursor < end {
            sum += end - cmp::max(cursor, start);
            cursor = end;
        }
    }
    println!("{}", sum);

    Ok(())
}
