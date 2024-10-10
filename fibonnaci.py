#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""

import argparse


def generate_fibonacci(limit):
    fibonacci_sequence = [0, 1]
    while True:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_value >= limit:
            break
        fibonacci_sequence.append(next_value)
    return fibonacci_sequence

def write_to_file(filename, data):

    try:
        with open(filename, 'w') as file:
            file.write(", ".join(map(str, data)))
            print(f"Successfully written Fibonacci numbers to {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Fibonacci numbers less than a limit and write to a file.")
    parser.add_argument("--limit", type=int, required=True, help="Upper limit for Fibonacci numbers")
    parser.add_argument("--output", type=str, required=True, help="Output file name")
    
    # Parse arguments
    args = parser.parse_args()

    # Generate Fibonacci numbers
    fibonacci_numbers = generate_fibonacci(args.limit)
    
    # Write Fibonacci numbers to the specified file
    write_to_file(args.output, fibonacci_numbers)