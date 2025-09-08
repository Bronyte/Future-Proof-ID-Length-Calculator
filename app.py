#!/usr/bin/env python3
"""
Future-Proof ID Length Calculator
Allows numeric-only or alphanumeric IDs with linear/exponential growth.
Includes input validation, exception handling, and improved dynamic terminal UI.
"""

import math
import sys

# ANSI color codes
WHITE = "\033[97m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"

def colored_input(prompt, cast_func=str, condition=lambda x: True, error_msg="Invalid input."):
    """Prompt user in white, input in yellow, cast type, and validate with condition."""
    while True:
        try:
            value = input(f"{WHITE}{prompt}{YELLOW} ").strip()
            if value == "":
                raise ValueError("Empty input.")
            value = cast_func(value)
            if not condition(value):
                raise ValueError("Condition failed.")
            return value
        except ValueError:
            print(f"{RED}{error_msg}{RESET}")

def main():
    print(f"{CYAN}{'='*50}")
    print(f"{GREEN}   Future-Proof ID Length Calculator")
    print(f"{CYAN}{'='*50}{RESET}\n")

    try:
        # Get validated inputs
        current_count = colored_input(
            "Enter current number of IDs:", int,
            condition=lambda x: x > 0,
            error_msg="Please enter a positive integer."
        )

        growth_type = colored_input(
            "Select growth type - linear (L) or exponential (E):", str,
            condition=lambda x: x.upper() in ['L', 'E'],
            error_msg="Please enter 'L' or 'E'."
        ).upper()

        growth_rate = colored_input(
            "Enter expected annual growth rate (e.g., 0.10 for 10%):", float,
            condition=lambda x: x >= 0,
            error_msg="Please enter a non-negative decimal (e.g., 0.10)."
        )

        duration_years = colored_input(
            "Enter duration in years:", int,
            condition=lambda x: x > 0,
            error_msg="Please enter a positive integer."
        )

        char_type = colored_input(
            "ID type: numeric only (N) or alphanumeric (A):", str,
            condition=lambda x: x.upper() in ['N', 'A'],
            error_msg="Please enter 'N' or 'A'."
        ).upper()

        safety_margin = colored_input(
            "Enter safety margin (extra digits/characters, e.g., 1 or 2):", int,
            condition=lambda x: x >= 0,
            error_msg="Please enter a non-negative integer."
        )

    except KeyboardInterrupt:
        print(f"\n{RED}Program interrupted by user.{RESET}")
        sys.exit(1)

    # Calculate projected maximum IDs
    if growth_type == 'E':
        projected_max = current_count * (1 + growth_rate) ** duration_years
    else:
        projected_max = current_count + (current_count * growth_rate * duration_years)

    # Determine characters needed
    if char_type == 'N':
        base = 10
        chars_needed = math.ceil(math.log10(projected_max)) if projected_max > 1 else 1
        final_length = chars_needed + safety_margin
        example_id = '0' * final_length
    else:
        base = 36  # 0-9 + A-Z
        chars_needed = math.ceil(math.log(projected_max, base)) if projected_max > 1 else 1
        final_length = chars_needed + safety_margin
        example_id = 'X' * final_length

    # Calculate total possible combinations
    total_combinations_without_margin = base ** chars_needed
    total_combinations_with_margin = base ** final_length
    extra_combinations_from_margin = total_combinations_with_margin - total_combinations_without_margin

    # Extra IDs relative to projection
    extra_ids_available = total_combinations_with_margin - projected_max
    extra_factor = total_combinations_with_margin / projected_max
    extra_percentage = (extra_ids_available / projected_max) * 100

    # Output in structured format
    print(f"\n{CYAN}{'-'*50}")
    print(f"{GREEN}Calculation Results:{RESET}")
    print(f"{GREEN}Projected maximum IDs: {PURPLE}{projected_max:.0f}{RESET}")
    print(f"{GREEN}Characters needed without safety margin: {PURPLE}{chars_needed}{RESET}")
    print(f"{GREEN}Characters needed with safety margin: {PURPLE}{final_length}{RESET}")
    print(f"{GREEN}Total possible IDs without safety margin: {PURPLE}{total_combinations_without_margin:,}{RESET}")
    print(f"{GREEN}Total possible IDs with safety margin: {PURPLE}{total_combinations_with_margin:,}{RESET}")
    print(f"{GREEN}Extra IDs provided by safety margin: {PURPLE}{extra_combinations_from_margin:,}{RESET}")
    print(f"{GREEN}Extra IDs above projection: {PURPLE}{extra_ids_available:,.0f}{RESET}")
    print(f"{GREEN}Capacity factor (possible ÷ projected): {PURPLE}{extra_factor:.2f}x{RESET}")
    print(f"{GREEN}Extra capacity percentage: {PURPLE}{extra_percentage:.1f}%{RESET}")
    if char_type == 'N':
        print(f"{GREEN}Example numeric ID: {PURPLE}{example_id}{RESET}")
    else:
        print(f"{GREEN}Example alphanumeric ID: {PURPLE}{example_id} (0-9, A-Z){RESET}")
    print(f"{CYAN}{'-'*50}{RESET}")

if __name__ == "__main__":
    main()
