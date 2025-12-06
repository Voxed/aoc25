use std::error::Error;
use std::io::{self, Read};

fn main() -> Result<(), Box<dyn Error>> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    input = input.replace("\r\n", "\n");

    let mut has_scroll = input
        .split('\n')
        .map(|l| l.chars().map(|c| c == '@').collect::<Vec<_>>())
        .filter(|l| !l.is_empty())
        .collect::<Vec<_>>();

    let mut sum = 0;
    loop {
        let removals = has_scroll
            .iter()
            .enumerate()
            .map(|(y, row)| {
                row.iter()
                    .enumerate()
                    .map(|(x, &scroll)| {
                        let count = (-1isize..2)
                            .map(|yd| {
                                (-1isize..2)
                                    .filter_map(|xd| {
                                        if xd == 0 && yd == 0 {
                                            return None;
                                        }
                                        let nx = (x as isize + xd) as usize;
                                        let ny = (y as isize + yd) as usize;
                                        let scroll = has_scroll
                                            .get(ny)
                                            .and_then(|r| r.get(nx))
                                            .copied()
                                            .unwrap_or(false);
                                        if scroll { Some(()) } else { None }
                                    })
                                    .count()
                            })
                            .sum::<usize>();
                        scroll && count < 4
                    })
                    .collect::<Vec<_>>()
            })
            .collect::<Vec<Vec<_>>>();
        let removal_count: usize = removals
            .iter()
            .flat_map(|r| r.iter())
            .filter(|&&b| b)
            .count();
        if removal_count == 0 {
            break;
        }
        if sum == 0 {
            println!("{}", removal_count);
        }
        sum += removal_count;
        has_scroll = has_scroll
            .iter()
            .zip(removals.iter())
            .map(|(s, r)| s.iter().zip(r).map(|(&s, &r)| s && !r).collect::<Vec<_>>())
            .collect::<Vec<Vec<_>>>();
    }
    println!("{}", sum);

    Ok(())
}
