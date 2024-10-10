#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

# You're on your own for this one. Good luck!

import argparse
from fibonnaci import generate_fibonacci

def is_prime(n):
    """Check if a number n is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # No other even numbers are prime
    for i in range(3, int(n ** 0.5), 2):
        if n % i == 0:
            return False
    return True

def find_largest_prime_fibonacci(limit):
    fibonacci_numbers = generate_fibonacci(limit)
    prime_fibonacci_numbers = [n for n in fibonacci_numbers if is_prime(n)]
    if prime_fibonacci_numbers:
        return max(prime_fibonacci_numbers)
    return None

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Find the largest prime Fibonacci number less than a given limit.")
    parser.add_argument("--limit", type=int, required=True, help="Upper limit for Fibonacci numbers")
    
    # Parse arguments
    args = parser.parse_args()

    # Find and print the largest prime Fibonacci number
    largest_prime = find_largest_prime_fibonacci(args.limit)
    if largest_prime:
        print(f"The largest prime Fibonacci number less than {args.limit} is: {largest_prime}")
    else:
        print(f"No prime Fibonacci numbers found below {args.limit}.")

# After running the .py file in command line, the largest prime Fibonacci number less that 50000 found to be 28657