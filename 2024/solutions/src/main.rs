use std::{env, process};

mod days;
mod common_utils;

const MESSAGE_USAGE: &str = "Usage: cargo run -- <DAY>";

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        println!("Error! Not enough arguments supplied. {}", MESSAGE_USAGE);
        process::exit(1);
    }

    let day_number = args[1].parse::<u8>().unwrap_or_else(|_| {
        println!("Error! Provided argument is not a number (requires a day number)");
        println!("{}", MESSAGE_USAGE);
        process::exit(1);
    });

    match day_number {
        1 => days::day_one::run(),
        _ => println!("Day {} not found!", day_number),
    }
}